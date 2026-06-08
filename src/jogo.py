import pygame

from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    FPS,
    TITULO_JOGO,
    CINZA,
    BRANCO,
    VERDE_MESA,
    AMARELO,
    CAMINHO_RECORDE,
    CAMINHO_SPRITES,
)

from src.funcoes import (
    calcular_pontos,
    jogador_perdeu,
    limitar_valor,
    verificar_colisao,
    tomar_dano,
)
from src.sprites import pegar_sprite
from src.dados import (
    salvar_recorde,
    carregar_recorde,
)


def executar_jogo():
    """Executa o loop principal do jogo e controla estado, colisões e pontuação."""
    pygame.init()
    

    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)

    pygame.font.init() #O pygame não carrega fontes automaticamente, então a gente tem que inicializar a fonte
    fonte_grande = pygame.font.SysFont("Arial", 64) 
    fonte_media  = pygame.font.SysFont("Arial", 32)

    estado = "menu"
    
    relogio = pygame.time.Clock()
    rodando = True

    # 1. Carregando as imagens recortadas do Spritesheet


    # Jogador: usando tamanho 110x110 para capturar o quadrado perfeitamente
    player_image = pegar_sprite(CAMINHO_SPRITES, x=110, y=120, width=190, height=190, scale=0.5)

    # Gema pequena: usando tamanho 64x64
    gem_image    = pegar_sprite(CAMINHO_SPRITES, x=900, y=690, width=200, height=200, scale=0.5)

    # Morcego: usando tamanho 180x120 por causa das asas abertas
    bat_image    = pegar_sprite(CAMINHO_SPRITES, x=905, y=1060, width=200, height=130, scale=0.5)
    
    # 2. Criando a estrutura de Sprites usando Dicionários
    jogador = {
        "imagem": player_image,
        "rect": player_image.get_rect(topleft=(100, 100))
    }

    gema = {
        "imagem": gem_image,
        "rect": gem_image.get_rect(topleft=(500, 300))
    }
    
    inimigo = {
        "imagem": bat_image,
        "rect": bat_image.get_rect(topleft=(200, 500))
    }
    carta = {
        "rect": pygame.Rect(LARGURA_TELA//2, ALTURA_TELA//2, 60, 90) # Temporário
    }

    velocidade = 5
    pontos = 0
    vidas = 3
    recorde = carregar_recorde(CAMINHO_RECORDE)

    # Loop principal: processa entrada, atualiza estado e renderiza a cena.
    while rodando:
        relogio.tick(FPS)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.KEYDOWN:
                if estado == "menu":
                    if evento.key == pygame.K_RETURN:
                        estado = "jogo"

        teclas = pygame.key.get_pressed()

        # Movimentação alterando direto os eixos X e Y do retângulo da carta
        if estado == "jogo":
            if teclas[pygame.K_LEFT]:
                carta["rect"].x -= velocidade
            if teclas[pygame.K_RIGHT]:
                carta["rect"].x += velocidade
            if teclas[pygame.K_UP]:
                carta["rect"].y -= velocidade
            if teclas[pygame.K_DOWN]:
                carta["rect"].y += velocidade
        # Limitando a carta dentro das bordas da tela usando as propriedades do Rect
        carta["rect"].x = limitar_valor(carta["rect"].x, 0, LARGURA_TELA - carta["rect"].width)
        carta["rect"].y = limitar_valor(carta["rect"].y, 0, ALTURA_TELA - carta["rect"].height)

        # Verificação de colisão com a Gema (antigo 'item')
        if verificar_colisao(jogador["rect"], gema["rect"]):
            pontos = calcular_pontos(pontos, 10)

            # Move a gema de lugar ao coletar
            gema["rect"].x += 80
            gema["rect"].y += 50

            # Se a gema sair da tela, volta para uma posição segura
            if gema["rect"].x > LARGURA_TELA - gema["rect"].width:
                gema["rect"].x = 50
            if gema["rect"].y > ALTURA_TELA - gema["rect"].height:
                gema["rect"].y = 50

        # Verificação de colisão com o Inimigo
        if verificar_colisao(jogador["rect"], inimigo["rect"]):
            vidas = tomar_dano(vidas, 1)

            # Afasta o inimigo ao colidir
            inimigo["rect"].x += 80
            inimigo["rect"].y += 50

            if inimigo["rect"].x > LARGURA_TELA - inimigo["rect"].width:
                inimigo["rect"].x = 50
            if inimigo["rect"].y > ALTURA_TELA - inimigo["rect"].height:
                inimigo["rect"].y = 50

        # Regras de fim de jogo e recorde
        if jogador_perdeu(vidas):
            rodando = False

        if pontos > recorde:
            recorde = pontos
            salvar_recorde(CAMINHO_RECORDE, recorde)

        pygame.display.set_caption(
            f"{TITULO_JOGO}"
        )

        if estado == "menu": # Vai ver se o jogo está no menu ainda, se estiver ele vai colar o título e a instrução para o jogador entrar no jogo
            tela.fill((VERDE_MESA))
            titulo = fonte_grande.render("BlackJack", True, (AMARELO))
            instrucao = fonte_media.render("Pressione ENTER para jogar", True, (BRANCO))
            tela.blit(titulo, titulo.get_rect(center=(LARGURA_TELA//2, 200))) # Utilizar // em vez de / porque o pygame só recebe valor inteiro
            tela.blit(instrucao, instrucao.get_rect(center=(LARGURA_TELA//2, 350))) # Utilizar // em vez de / porque o pygame só recebe valor inteiro
            # O blit é como se fosse vc colasse figuras uma em cima da outra, então nesse caso você cola em cima da tela o título e a instrução

        elif estado == "jogo": # Vai ver se o jogo agora saiu do menu e foi para a tela de jogar, se estiver ele vai colar na tela só o texto padrão que deixamos
            tela.fill((VERDE_MESA))
            pygame.draw.rect(tela, BRANCO, carta["rect"])
            texto = fonte_media.render("MESA DE JOGO", True, (BRANCO))
            tela.blit(texto, texto.get_rect(center=(LARGURA_TELA//2, ALTURA_TELA//2)))

        pygame.display.flip()

    pygame.quit()
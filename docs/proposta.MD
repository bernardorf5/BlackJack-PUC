# Proposta Inicial do Jogo

## 1. Nome provisório do jogo

> BlackJack PUC

## 2. Integrantes do grupo

- Nome 1: Bernardo Ramos Ferreira
- Nome 2: Gabriel de Oliveira Costa
- Nome 3: Francisco de Castro Côrtes Netto
- Nome 4: Theo Goulart Cardoso Vasconcelos

## 3. Tipo de jogo

Tipo escolhido pelo grupo:

> Jogo de cartas — BlackJack (21)

## 4. Descrição geral do jogo

Descrição:

> O jogo vai simular uma partida de BlackJack entre o jogador e um dealer controlado pelo computador. O jogador irá receber cartas de um baralho padrão de 52 cartas e a cada rodada, deve decidir se pede mais uma carta (Hit) ou para de comprar (Stand), com o objetivo de somar os valores das cartas o mais perto de 21.

## 5. Objetivo do jogador

Objetivo:

> Chegar o mais perto possível de 21 pontos com as cartas na mão, sem ultrapassar esse valor, e ter uma pontuação maior do que o dealer ao final da rodada.

## 6. Regras principais

Regras do grupo:

- Regra 1: O jogador e o dealer recebem 2 cartas no início de cada rodada, e uma carta do dealer fica virada para baixo.
- Regra 2: Cartas de figuras valem 10; Às valem 1 ou 11, qual for mais vantajosa.
- Regra 3: O jogador pode pedir mais cartas (Hit) quantas vezes quiser (Sem estourar) ou parar (Stand).
- Regra 4: Após o jogador parar, o dealer revela sua carta escondida e compra cartas até atingir pelo menos 17 pontos.
- Regra 5: Quem estourar (ultrapassar 21) ou tiver a menor quantidade de pontos perde.

## 7. Condição de vitória

Condição de vitória:

> Tiver uma pontuação maior do que o dealer sem ultrapassar 21; Ou o dealer estourar (ultrapassar 21) enquanto o jogador não tiver estourado.  

## 8. Condição de derrota ou encerramento

Condição de derrota ou encerramento:

> O jogador perde se estourar (ultrapassar 21); O jogador perde se o dealer tiver pontuação maior ao final da rodada; Empate ocorre quando tanto o dealer quanto o jogador terminam com a mesma pontuação; A partida encerra quando o jogador ficar sem fichas, ou quando escolher sair.

## 9. Elementos previstos no jogo

## Jogador ou elemento principal

Descrição:

> O jogador é representado pela sua mão de cartas, exibida na parte inferior da tela. Ele toma decisões a cada rodada clicando nos botões de ação disponíveis na interface. 

## Obstáculos, inimigos ou desafios

Descrição:

> O principal desafio é o dealer, controlado pelo computador, e também a aleatoriedade das cartas geradas.

## Itens, alvos ou objetos de interação

Descrição:

> As cartas são os principais objetos de interação; Os botões Hit e Stand são os elementos de interação direta com o jogo; As fichas também são objetos de interação. O jogador clica nelas para definir o valor da aposta antes de cada rodada.

## Pontuação, vidas, tempo ou progresso

Descrição:

> O jogador começa com um saldo inicial de fichas, e aposta uma quantidade a cada rodada. Vitórias aumentam o saldo; derrotas diminuem. O progresso é medido pelo saldo atual e pelo recorde salvo em arquivo. A partida encerra quando o saldo chegar a zero.

## 10. Controles previstos

Informe os comandos que serão utilizados pelo jogador.

Controles do grupo:

- Tecla/comando: Clique do mouse no botão Hit: pedir mais uma carta
- Tecla/comando: Clique do mouse no botão Stand: parar de comprar cartas
- Tecla/comando: Clique do mouse no botão Nova Rodada: iniciar uma nova rodada após o resultado
- Tecla/comando: Clique do mouse nas fichas de aposta: selecionar o valor a ser apostado na rodada
- Tecla/comando: Clique do mouse no botão Confirmar Aposta: confirmar o valor apostado e iniciar a distribuição das cartas
- Tecla/comando: ESC: sair do jogo

## 11. Organização inicial do código

Organização planejada:

> `main.py`: inicia o jogo e chama o loop principal;
> `src/jogo.py`: contém o loop principal e o controle de estados do jogo (início, rodada, resultado);
> `src/baralho.py`: contém as funções de criação, embaralhamento e distribuição de cartas;
> `src/logica.py`: contém as funções de lógica do BlackJack (calcular pontuação, verificar bust (estourar), lógica do dealer (comprar até 17), determinar vencedor);
> `src/interface.py`: contém as funções de renderização da tela, cartas e botões com Pygame;
> `src/config.py`: guarda configurações globais como tamanho da tela, cores e saldo inicial;
> `src/arquivos.py`: contém funções de leitura e escrita do recorde em arquivo;
> `tests/test_logica.py`: contém os testes das funções de lógica do jogo.


## 12. Recursos externos previstos

Recursos previstos:

> Imagens de cartas obtidas de banco de assets gratuito (ex.: OpenGameArt), com licença livre; Fonte personalizada para a interface, obtida do Google Fonts;

## 13. Principais dificuldades esperadas

Dificuldades previstas:

- Dificuldade 1: Diferir os diferentes estados de jogo na tela, por exemplo, quando está sendo realizada uma aposta, de quando uma rodada está em andamento.
- Dificuldade 2: Implementar o sistema do Às podendo valer 1 ou 11 dependendo da pontuação.
- Dificuldade 3: Posicionar os sprites corretamente na tela.

## 14. Escopo mínimo para a entrega final

Escopo mínimo:

> A versão mínima do jogo terá: baralho embaralhado e distribuição de cartas, ações de Hit e Stand implementadas, lógica do dealer, lógica do Às, verificação e exibição do resultado de cada rodada (vitória, derrota ou empate) e sistema de fichas.

## 15. Possíveis melhorias, caso haja tempo

Melhorias possíveis:

- Melhoria 1: Tela inicial com menu.
- Melhoria 2: Efeitos sonoros para algumas das ações. Exemplo: Comprar cartas, ganhar, perder, apostar fichas, etc.
- Melhoria 3: Ranking das maiores pontuações.
- Melhoria 4: Sistema de double e split.

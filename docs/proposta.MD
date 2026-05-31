# Proposta Inicial do Jogo

Este documento deve ser preenchido pelo grupo na Semana 1 do projeto.

A proposta deve apresentar uma ideia simples, clara e viável para ser desenvolvida com Python e Pygame dentro do prazo disponível.

## 1. Nome provisório do jogo

#### > **_Pyquiz_**

## 2. Integrantes do grupo

Liste os integrantes do grupo.

- Nome 1: Lucas Elias Gonçalves Peixoto Lelis de Oliveira
- Nome 2:
- Nome 3:
- Nome 4:

## 3. Tipo de jogo

#### > Jogo de Perguntas e Respostas (Quiz) sobre a linguagem Python, com seleção de dificuldade e sistema de pontuação por tempo, desenvolvido com Python e a biblioteca proposta pygame()

Tipo escolhido pelo grupo:

## 4. Descrição geral do jogo

Explique, em poucas linhas, como o jogo funcionará.

Procure responder:

- O que aparece na tela?
- O que o jogador controla?
- O que o jogador precisa fazer?
- Quais desafios aparecem durante a partida?

Descrição:

#### > O PyQuiz é um jogo de quiz sobre a linguagem Python desenvolvido com a biblioteca Pygame. Ao iniciar, o jogador visualiza uma tela de seleção com três níveis de dificuldade: Fácil, Médio e Difícil. Após escolher o nível, o jogo apresenta uma sequência de perguntas de múltipla escolha com quatro alternativas cada, relacionadas ao conteúdo visto na disciplina.

> Na tela de jogo aparecem:

- A pergunta atual e suas quatro alternativas (A, B, C, D)
- Um temporizador regressivo de 15 a 20 segundos por questão
- Uma barra de progresso indicando o avanço no quiz
- O placar em tempo real (acertos e pontuação acumulada)
- Quando a questão envolve código Python, um bloco de código é exibido em destaque

O jogador usurá o mouse para selecionar a resposta clicando ou poderá usar a tecla correspondente (A/B/C/D) de acordo com as alternativas. Após responder (ou ao fim do tempo proposto), o jogo exibirá o feedback visual imediato: Verde para acerto ou vermelhor para erro, como também, a explicação da resposta correta. Ao final das questões, é exibida a tela de resultado com a pontuação total e um histórico das respostas;

## 5. Objetivo do jogador

Exemplos:

- coletar o maior número possível de itens;
- sobreviver pelo maior tempo possível;
- chegar até o final do labirinto;
- acertar alvos;
- responder perguntas corretamente;
- evitar obstáculos;
- quebrar todos os blocos.

Objetivo:

#### > Responder corretamente o maior número possível de perguntas sobre Python no menor tempo possível, acumulando a maior pontuação antes que o tempo de cada questão se esgote. Em modo multijogador (até 3 jogadores), vence quem terminar o quiz com maior pontuação total.

aqui.

## 6. Regras principais

Liste as principais regras do jogo.

Exemplo:

- O jogador começa com 3 vidas.
- Cada moeda coletada vale 10 pontos.
- Cada colisão com obstáculo remove 1 vida.
- A partida termina quando as vidas chegam a zero.
- O jogador vence se alcançar 100 pontos.

Regras do grupo:

- Regra 1:
- Regra 2:
- Regra 3:
- Regra 4:
- Regra 5:

#### **Regra 1**:. Cada partida apresenta 15 questões sorteadas aleatoriamente do banco de questões conforme a dificuldade escolhida.

#### **Regra 2**. Cada questão possui um tempo limite de 15 a 20 segundos (variando conforme a dificuldade).

#### **Regra 3**. Responder corretamente dentro do tempo concede pontos; quanto menos tempo usado, mais pontos o jogador recebe.

#### **Regra 4**. Não responder dentro do prazo conta como erro (0 pontos naquela questão).

#### **Regra 5.** Ao errar ou deixar o tempo esgotar, a resposta correta é revelada com explicação.

#### **Regra 6.** O jogo termina ao concluir todas as 15 questões ou quando o jogador encerrar a partida.

#### **Regra 7.** Em modo de 3 jogadores, cada jogador joga sequencialmente; vence quem acumular mais pontos.

## 7. Condição de vitória

Explique como o jogador vence ou conclui o jogo.

Exemplos:

- atingir determinada pontuação;
- chegar ao final da fase;
- sobreviver até o tempo acabar;
- responder uma quantidade mínima de perguntas;
- quebrar todos os blocos.

Condição de vitória:

#### > O jogador vence ao concluir todas as 15 questões com aproveitamento igual ou superior a 70% (pelo menos 11 acertos). Em modo multijogador, vence o jogador com a maior pontuação total ao fim das rodadas. O sistema registra o melhor desempenho em um arquivo de ranking.

## 8. Condição de derrota ou encerramento

Explique como o jogador perde ou quando a partida termina.

Exemplos:

- perder todas as vidas;
- acabar o tempo;
- colidir com determinado obstáculo;
- errar muitas perguntas;
- deixar a bola cair, no caso de Breakout ou Pong.

Condição de derrota ou encerramento:

#### > A partida encerra quando todas as 15 questões forem respondidas (com ou sem acerto) ou quando o tempo de todas as questões se esgotar. Não há condição de derrota imediata; o encerramento é natural ao final do quiz, com exibição da pontuação final e classificação (aprovado/reprovado conforme o aproveitamento).

## 9. Elementos previstos no jogo

Descreva os principais elementos que farão parte do jogo.

## Jogador ou elemento principal

#### **Exemplo:** O jogador interage com o jogo por meio do mouse (clique nas alternativas) e do teclado (teclas A, B, C, D para selecionar as respostas, e Enter para confirmar). Não há personagem visual, o protagonismo é do conteúdo das perguntas.

## Obstáculos, inimigos ou desafios

Exemplo:

> Obstáculos aparecem em posições aleatórias e devem ser evitados.

Descrição:

#### > O principal desafio é o temporizador regressivo, que pressiona o jogador a pensar e responder rapidamente. Questões com trechos de código Python adicionam uma camada extra de dificuldade, exigindo leitura e interpretação do código antes de responder.

## Itens, alvos ou objetos de interação

Exemplo:

> Moedas aparecem na tela e aumentam a pontuação quando coletadas.

Descrição:

#### > As alternativas de resposta são os elementos de interação principais. Questões que exibem blocos de código funcionam como "itens de contexto" que o jogador deve analisar para escolher a alternativa correta.

## Pontuação, vidas, tempo ou progresso

Exemplo:

> O jogador começa com 3 vidas e ganha 10 pontos por item coletado.

Descrição:

#### • Pontuação baseada em acertos e no tempo restante ao responder

#### • Sem sistema de vidas — todas as questões são respondidas independentemente do desempenho

#### • Temporizador por questão: 20s (Fácil), 15s (Médio), 12s (Difícil)

#### • Barra de progresso mostrando questão atual / total de questões

#### • Ranking salvo em arquivo .txt ou .json ao final de cada partida

## 10. Controles previstos

Informe os comandos que serão utilizados pelo jogador.

Exemplo:

- Seta para cima: mover para cima
- Seta para baixo: mover para baixo
- Seta para esquerda: mover para esquerda
- Seta para direita: mover para direita
- Espaço: realizar ação
- ESC: sair do jogo

Controles do grupo:

- Tecla/comando:
- Tecla/comando:
- Tecla/comando:

- Teclas A / B / C / D: selecionar a alternativa correspondente
- Clique do mouse: selecionar alternativa clicando no botão visual
- Enter ou Espaço: confirmar seleção e avançar para a próxima questão
- ESC: pausar o jogo ou voltar ao menu principal
- Setas direcionais (↑↓): navegar entre as alternativas

## 11. Organização inicial do código

Explique como o grupo pretende organizar o código.

Exemplo:

- `main.py`: inicia o jogo;
- `src/jogo.py`: contém o loop principal;
- `src/config.py`: guarda configurações como tamanho da tela e cores;
- `src/funcoes.py`: contém funções auxiliares;
- `src/dados.py`: contém funções de leitura e escrita de arquivos.

Organização planejada:

- • main.py — ponto de entrada; inicializa o Pygame e chama o menu principal
- • src/config.py — constantes globais: resolução da tela, cores, FPS, tempo por questão
- • src/menu.py — tela inicial com seleção de dificuldade e menu de opções
- • src/jogo.py — loop principal do quiz: exibição de perguntas, temporizador, feedback
- • src/resultado.py — tela de resultado final com pontuação e histórico de respostas
- • src/ranking.py — leitura e escrita do ranking em arquivo (leitura/escrita de arquivos)
- • src/questoes.py — carregamento e gerenciamento do banco de questões (listas e dicionários)
- • data/questoes.json — banco de questões organizado por dificuldade (arquivo de dados)
- • data/ranking.txt — arquivo de ranking persistente entre partidas
- • assets/ — fontes, ícones e sons (caso eu implemente)

## 12. Recursos externos previstos

Informe se o grupo pretende utilizar imagens, sons, fontes, tutoriais ou códigos externos.

Exemplo:

- imagens obtidas de banco gratuito;
- sons gratuitos;
- tutorial usado apenas como referência;
- fonte personalizada.

Recursos previstos:

- • Fonte personalizada gratuita
- • Sons de feedback (acerto/erro/temporizador) obtidos de bancos de áudio gratuitos (ex: OpenGameArt)
- • Banco de questões desenvolvido pelo grupo com base nos slides e listas da disciplina
- • Documentação oficial do Pygame (pygame.org) usada apenas como referência técnica

Caso não pretenda utilizar recursos externos, escreva:

> Não pretendemos utilizar recursos externos.

## 13. Principais dificuldades esperadas

Liste as dificuldades que o grupo acredita que poderá enfrentar.

Exemplos:

- movimentação do jogador;
- colisão entre objetos;
- controle de tempo;
- criação do ranking;
- organização do código;
- uso do GitHub;
- testes;
- exibição de textos na tela.

Dificuldades previstas:

- Dificuldade 1: Implementar o temporizador por questão de forma precisa e integrada ao loop do Pygame
- Dificuldade 2: Renderizar blocos de código Python formatados dentro da janela do Pygame (quebra de linha, fonte monoespaçada)
- Dificuldade 3: Organizar e carregar o banco de questões em JSON de forma eficiente, garantindo aleatoriedade sem repetição
- Dificuldade 4: Implementar o modo multijogador sequencial com controle de turno e placar individual
- Dificuldade 5: Manter a modularização clara do código com múltiplos arquivos funcionando em conjunto

## 14. Escopo mínimo para a entrega final

Descreva qual será a versão mínima aceitável do jogo.

Esta seção é importante para evitar que o grupo escolha uma ideia grande demais.

Exemplo:

> A versão mínima do jogo terá um personagem controlado pelo teclado, obstáculos aparecendo na tela, sistema de vidas, sistema de pontuação e tela de fim de jogo.

Escopo mínimo:

#### > A versão mínima do PyQuiz terá: tela de menu com seleção de dificuldade (Fácil, Médio, Difícil), 15 questões de múltipla escolha carregadas de arquivo, temporizador por questão, sistema de pontuação, feedback visual de acerto/erro, tela de resultado com aproveitamento percentual, e salvamento do ranking em arquivo.

## 15. Possíveis melhorias, caso haja tempo

Liste funcionalidades extras que o grupo poderá implementar se conseguir concluir o escopo mínimo.

Exemplos:

- tela inicial;
- sons;
- fases;
- aumento de dificuldade;
- ranking;
- animações;
- novos tipos de obstáculos;
- diferentes personagens;
- menu de pausa.

Melhorias possíveis:

- Melhoria 1:
- Melhoria 2:
- Melhoria 3:

#### • Modo multijogador local para até 3 jogadores com placar comparativo

#### • Questões de código aberto: exibir um trecho com erro e pedir ao jogador que identifique a linha incorreta

#### • Efeitos sonoros e trilha sonora de fundo

#### • Tela de ranking persistente com os 10 melhores resultados

#### • Animações de transição entre questões e telas

#### • Geração de relatório PDF ou TXT com o desempenho detalhado ao final da partida

#### • Integração com IA para geração dinâmica de novas questões (modo ilimitado)

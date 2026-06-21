# PyQuiZ´s 🐍

Projeto final da disciplina de Introdução a Algoritmos/Programação, desenvolvido com Python e Pygame.

Este repositório é um template para os grupos da disciplina. A proposta é começar com uma base funcional e evoluir o jogo ao longo do semestre.

## > Integrantes do grupo

- Lucas Elias Gonçalves Peixoto Lelis de Oliveira

## Estrutura do projeto

- `main.py`: ponto de entrada da aplicação.
- `src/`: código-fonte principal do jogo (loop, regras, sprites e dados).
- `assets/`: imagens, fontes e sons.
- `data/`: arquivos persistentes (recorde/ranking).
- `tests/`: testes unitários com `pytest`.
- `docs/`: documentação do projeto, incluindo proposta inicial.

## > Descrição do jogo


#### ***O PyQuiz é um jogo de quiz sobre a linguagem Python.*** 
#### Ao iniciar, o jogador visualiza uma tela de seleção com três níveis de dificuldade: **Fácil**, **Médio** e **Difícil**. Após escolher o nível, o jogo apresenta uma sequência de perguntas de múltipla escolha com quatro alternativas cada, relacionadas ao conteúdo visto na disciplina.

#### > Na tela de jogo aparecem:

- A pergunta atual e suas quatro alternativas (A, B, C, D).
- Um temporizador regressivo por questão (variando conforme a dificuldade).
- Uma barra de progresso indicando o avanço no quiz.
- O placar em tempo real (pontuação acumulada).
- Quando a questão envolve código Python, um bloco de código é exibido em destaque.

#### O jogador usa as setas do teclado para navegar entre as alternativas e ENTER para confirmar. Após responder (ou ao fim do tempo), o jogo exibe feedback visual imediato:  verde para acerto, vermelho para erro; Além da explicação da resposta correta. Ao final das questões, é exibida a tela de resultado com a pontuação total, o aproveitamento percentual e o recorde salvo.

## > Objetivo do jogador

#### Responder corretamente o maior número possível de perguntas sobre Python dentro do tempo limite de cada questão, acumulando a maior pontuação possível antes do fim do quiz. O bônus de pontuação é maior quanto mais rápido o jogador responde corretamente.


## > Regras do jogo

> **1.** Cada partida apresenta as questões do banco de dados, sorteadas conforme a dificuldade escolhida.
> **2.** Cada questão possui um tempo limite que varia por dificuldade: 30s (Fácil), 20s (Médio), 15s (Difícil).
> **3.** Responder corretamente dentro do tempo concede pontos; quanto menos tempo usado, maior o bônus.
> **4.** Não responder dentro do prazo conta como erro (0 pontos naquela questão).
> **5.** Ao errar ou esgotar o tempo, a resposta correta é revelada com explicação.
> **6.** O jogo termina ao concluir todas as questões da partida.

## > Condição de vitória

#### O jogador é considerado **aprovado** ao concluir a partida com aproveitamento igual ou superior a 70%. O sistema registra a maior pontuação alcançada em um arquivo de recorde, e o histórico de cada partida é salvo em um arquivo de ranking.

## > Condição de encerramento

#### A partida encerra naturalmente quando todas as questões forem respondidas (com ou sem acerto). Não há condição de derrota imediata — ao final, é exibida a pontuação, o aproveitamento percentual e a classificação (aprovado/reprovado).
## Controles

## Controles

| Tecla | Ação |
|---|---|
| **Setas ESQUERDA/DIREITA** | Navegar entre as dificuldades no menu |
| **Setas CIMA/BAIXO** | Navegar entre as alternativas / botões de resultado |
| **ENTER** | Confirmar seleção / avançar |
| **ESC** | Voltar ao menu ou sair do jogo |

## > Organização do código:

PyQuiz/

├── main.py                 # ponto de entrada; inicializa o Pygame

├── requirements.txt        # dependências do projeto

├── src/

│   ├── config.py           # constantes globais: tela, cores, FPS, tempo por questão

│   ├── jogo.py             # loop principal: menu, perguntas, temporizador, resultado

│   ├── funcoes.py          # funções auxiliares de lógica (pontos, limites, aproveitamento)

│   ├── dados.py            # leitura/escrita de arquivos (recorde, ranking, questões)

│   └── ui.py               # funções de desenho da interface (cards, chips, barras, sombras)

├── data/

│   ├── questoes.json        # banco de questões organizado por dificuldade

│   ├── recorde.txt          # maior pontuação já alcançada

│   └── ranking.txt          # histórico de partidas (nome;pontos;dificuldade)

├── tests/

│   └── test_logica.py       # testes automatizados das funções de lógica

└── docs/

└── proposta.MD              # proposta inicial do projeto (Semana 1)

## Como executar o projeto

### > Recursos externos previstos

#### Banco de questões desenvolvido com base no conteúdo da disciplina. Documentação oficial do Pygame (pygame.org) usada apenas como referência técnica.

> **Sobre assets visuais:** este projeto não utiliza imagens, sons ou fontes externas como arquivo. Todos os elementos visuais (cards, barras de progresso, textos, formas) são desenhados via código com as primitivas gráficas do Pygame (`pygame.draw`, `pygame.font.SysFont`). As fontes usadas (Segoe UI e Consolas) são fontes padrão do sistema operacional.

## Como executar o projeto

```bash
git clone https://github.com/Lulelis/IntroAlgs_pygame_template.git
cd IntroAlgs_pygame_template
py -3.12 -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
python main.py
```

## Como executar os testes

```bash
python -m pytest
```

## Melhorias planejadas para versões futuras

> As funcionalidades abaixo fazem parte da proposta inicial do projeto, mas **ainda não foram implementadas** na versão atual:

- Modo multijogador local para até 3 jogadores, com placar comparativo e disputa por melhor tempo/pontuação.

- Questões de código aberto: exibir um trecho de código com erro e pedir ao jogador que identifique a linha incorreta ou preveja a saída.

- Efeitos sonoros e trilha sonora de fundo.

- Tela de ranking persistente exibindo os melhores resultados dentro do próprio jogo.

- Animações de transição entre telas.

- Expansão do banco de questões com base em material adicional da disciplina (slides e listas de exercícios).

## Integrantes do grupo

- Lucas Elias Gonçalves Peixoto Lelis de Oliveira

## Checklist mínimo para entrega

- Preencher este README com nome final, descrição real, regras e controles do jogo.
- Atualizar `docs/proposta.MD` com a proposta do grupo.
- Garantir que o jogo executa com `python main.py`.
- Garantir que os testes passam com `pytest`.

## Observações para os alunos

- Mantenham o código organizado em módulos pequenos e com responsabilidade clara.
- Comentem partes importantes da lógica, principalmente regras do jogo.
- Registrem decisões técnicas no README do grupo ao longo do desenvolvimento.

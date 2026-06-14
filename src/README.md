# PyQuiz 🐍

> Quiz de perguntas e respostas sobre a linguagem Python, desenvolvido com Python e Pygame.


## Como executar:

- 1. Clone este repositório
- 2. Crie o ambiente Virtual

py -3.12 -m venv ven

- 3. Ative o ambiente virtual:

venv\Scripts\activate.bat

- 4. Instale as dependências:

pip install -r requeriments.txt

- 5. Execute o jogo:

python main.py

### Breve instruções de como jogar!⚽

- **Setas ↑↓** — navegar entre as opções
- **Enter** — confirmar seleção
- **ESC** — voltar ao menu ou sair

### Dificuldades:

| Nível | Tempo por questão |
|--|------------------------|
|Fácil | 30 segundos |
| Médio | 20 segundos|
| Difícil | 15 segundos|

### Estrutura do projeto

PyQuiz/

├── main.py

├── requirements.txt

├── src/

│   ├── config.py       ### Configurações gerais

│   ├── jogo.py         ### Loop principal

│   ├── funcoes.py      ### Funções auxiliares

│   └── dados.py        ### Leitura e escrita de arquivos

├── data/

│   ├── questoes.json   ### Banco de questões

│   ├── recorde.txt     ### Recorde salvo

│   └── ranking.txt     ### Ranking das partidas

├── tests/

│   └── test_logica.py  ### Testes automatizados

└── docs/

└── proposta.MD     ### Proposta do projeto

### Testes:

python -m pytest tests/test_logica.py -v

## Integrantes:

- Lucas Elias Gonçalves Peixoto Lelis de Oliveira

## Arquivos

- `jogo.py`: loop principal, eventos, atualização e renderização.
- `config.py`: constantes globais (tela, cores, caminhos, FPS).
- `funcoes.py`: funções auxiliares de regra e lógica.
- `sprites.py`: carregamento e recorte de spritesheet.
- `dados.py`: leitura e gravação de dados (recorde/ranking).

## Dica de evolução

Quando o projeto crescer, mantenha módulos pequenos e separados por responsabilidade.

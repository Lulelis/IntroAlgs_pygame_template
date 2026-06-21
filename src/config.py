# src/config.py
# Configurações centrais do PyQuiz

# --- Tela ---
LARGURA_TELA = 800
ALTURA_TELA = 640
FPS = 60
TITULO_JOGO = "PyQuiz - Quiz de Python"

# --- Paleta dark (estilo do protótipo) ---
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

FUNDO = (15, 15, 23)  # fundo principal (quase preto azulado)
FUNDO_CARD = (22, 22, 31)  # fundo dos cards/menus
FUNDO_CARD_2 = (30, 30, 46)  # fundo um pouco mais claro (hover/selecionado)
BORDA = (42, 42, 62)  # borda padrão sutil
BORDA_CLARA = (58, 58, 85)  # borda destacada

TEXTO = (205, 214, 244)  # texto principal (quase branco azulado)
TEXTO_FRACO = (127, 132, 156)  # texto secundário (cinza azulado)

AZUL = (137, 180, 250)  # destaque principal
AZUL_FUNDO = (26, 37, 64)  # fundo de elementos azuis

VERDE = (166, 227, 161)  # fácil / acerto
VERDE_FUNDO = (13, 42, 31)

AMARELO = (249, 226, 175)  # médio
AMARELO_FUNDO = (42, 32, 16)

VERMELHO = (243, 139, 168)  # difícil / erro
VERMELHO_FUNDO = (42, 16, 32)

ROXO = (203, 166, 247)  # detalhes / logo

# --- Cores antigas (compatibilidade, se ainda usadas em algum lugar) ---
CINZA = (212, 212, 212)
CINZA_ESCURO = FUNDO
AZUL_CLARO = AZUL
BRANCO_GELO = TEXTO

# --- Arquivos ---
CAMINHO_RECORDE = "data/recorde.txt"
CAMINHO_RANKING = "data/ranking.txt"
CAMINHO_QUESTOES = "data/questoes.json"

# --- Jogo ---
TOTAL_QUESTOES = 15
TEMPO_FACIL = 30
TEMPO_MEDIO = 20
TEMPO_DIFICIL = 15

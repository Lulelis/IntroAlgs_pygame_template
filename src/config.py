# src/config.py
# Configurações centrais do PyQuiz

# --- Tela ---
LARGURA_TELA = 800
ALTURA_TELA = 600
FPS = 60
TITULO_JOGO = "PyQuiz - Quiz de Python"

# --- Cores ---
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
CINZA = (212, 212, 212)
CINZA_ESCURO = (40, 40, 40)
AZUL = (52, 101, 164)
AZUL_CLARO = (114, 159, 207)
VERDE = (78, 154, 6)
VERMELHO = (204, 0, 0)
AMARELO = (237, 212, 0)
BRANCO_GELO = (238, 238, 238)

# --- Arquivos ---
CAMINHO_RECORDE = "data/recorde.txt"
CAMINHO_RANKING = "data/ranking.txt"
CAMINHO_QUESTOES = "data/questoes.json"

# --- Jogo ---
TOTAL_QUESTOES = 15
TEMPO_FACIL = 20  # segundos por questão
TEMPO_MEDIO = 15
TEMPO_DIFICIL = 12

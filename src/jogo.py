# src/jogo.py
# Loop principal do PyQuiz - Semana 3

import pygame

# src/jogo.py
# Loop principal do PyQuiz - Semana 3
from src.config import (
    ALTURA_TELA,
    AMARELO,
    AZUL,
    AZUL_CLARO,
    BRANCO,
    BRANCO_GELO,
    CAMINHO_QUESTOES,
    CAMINHO_RANKING,
    CAMINHO_RECORDE,
    CINZA_ESCURO,
    FPS,
    LARGURA_TELA,
    TEMPO_DIFICIL,
    TEMPO_FACIL,
    TEMPO_MEDIO,
    TITULO_JOGO,
    VERDE,
    VERMELHO,
)
from src.dados import (
    carregar_questoes,
    carregar_recorde,
    salvar_ranking,
    salvar_recorde,
)
from src.funcoes import (
    calcular_pontos,
    limitar_valor,
)


def desenhar_texto(tela, texto, tamanho, cor, x, y, centralizado=False):
    # """Renderiza texto na tela na posição indicada."""
    fonte = pygame.font.SysFont("arial", tamanho)
    superficie = fonte.render(texto, True, cor)
    rect = superficie.get_rect()
    if centralizado:
        rect.centerx = x
    else:
        rect.x = x
    rect.y = y
    tela.blit(superficie, rect)


def desenhar_menu(tela, opcao_selecionada):
    # """Desenha a tela inicial com as opções de dificuldade."""
    tela.fill(CINZA_ESCURO)

    desenhar_texto(
        tela, "PyQuiz", 64, AMARELO, LARGURA_TELA // 2, 60, centralizado=True
    )
    desenhar_texto(
        tela,
        "Quiz de Python",
        24,
        AZUL_CLARO,
        LARGURA_TELA // 2,
        140,
        centralizado=True,
    )
    desenhar_texto(
        tela,
        "Escolha a dificuldade:",
        20,
        BRANCO,
        LARGURA_TELA // 2,
        210,
        centralizado=True,
    )

    opcoes = [
        "Facil  (20s por questao)",
        "Medio  (15s por questao)",
        "Dificil (12s por questao)",
    ]
    cores_opcao = [VERDE, AMARELO, VERMELHO]

    for i, (nome, cor) in enumerate(zip(opcoes, cores_opcao)):
        y = 265 + i * 70
        cor_fundo = AZUL if i == opcao_selecionada else (60, 60, 60)
        pygame.draw.rect(tela, cor_fundo, (150, y, 500, 50), border_radius=10)
        pygame.draw.rect(tela, cor, (150, y, 500, 50), width=2, border_radius=10)
        desenhar_texto(
            tela, nome, 22, cor, LARGURA_TELA // 2, y + 13, centralizado=True
        )

    desenhar_texto(
        tela,
        "Setas UP/DOWN para navegar  |  ENTER para confirmar",
        15,
        AZUL_CLARO,
        LARGURA_TELA // 2,
        490,
        centralizado=True,
    )
    desenhar_texto(
        tela,
        "ESC para sair",
        14,
        (150, 150, 150),
        LARGURA_TELA // 2,
        515,
        centralizado=True,
    )


def desenhar_pergunta(
    tela,
    numero,
    total,
    pergunta,
    opcoes,
    selecionada,
    acertou,
    respondeu,
    correta,
    tempo_restante,
    tempo_total,
):
    # """Desenha a pergunta atual, alternativas, temporizador e progresso."""
    tela.fill(CINZA_ESCURO)

    # Cabeçalho: questão e pontos
    desenhar_texto(tela, f"Questao {numero} de {total}", 18, AZUL_CLARO, 20, 12)

    # Temporizador
    cor_tempo = (
        VERDE
        if tempo_restante > tempo_total * 0.5
        else AMARELO
        if tempo_restante > tempo_total * 0.25
        else VERMELHO
    )
    desenhar_texto(tela, f"{tempo_restante}s", 22, cor_tempo, LARGURA_TELA - 70, 10)

    # Barra de progresso das questões
    largura_barra = int((numero / total) * (LARGURA_TELA - 40))
    pygame.draw.rect(
        tela, (60, 60, 60), (20, 38, LARGURA_TELA - 40, 8), border_radius=4
    )
    pygame.draw.rect(tela, AZUL, (20, 38, largura_barra, 8), border_radius=4)

    # Barra do temporizador
    largura_tempo = int((tempo_restante / tempo_total) * (LARGURA_TELA - 40))
    pygame.draw.rect(
        tela, (60, 60, 60), (20, 50, LARGURA_TELA - 40, 6), border_radius=4
    )
    pygame.draw.rect(tela, cor_tempo, (20, 50, largura_tempo, 6), border_radius=4)

    # Pergunta — quebra linha se for muito longa
    palavras = pergunta.split()
    linha1 = ""
    linha2 = ""
    for palavra in palavras:
        if len(linha1) + len(palavra) < 60:
            linha1 += palavra + " "
        else:
            linha2 += palavra + " "

    desenhar_texto(
        tela, linha1.strip(), 20, BRANCO_GELO, LARGURA_TELA // 2, 75, centralizado=True
    )
    if linha2.strip():
        desenhar_texto(
            tela,
            linha2.strip(),
            20,
            BRANCO_GELO,
            LARGURA_TELA // 2,
            100,
            centralizado=True,
        )

    # Alternativas
    letras = ["A", "B", "C", "D"]
    for i, (letra, opcao) in enumerate(zip(letras, opcoes)):
        y = 145 + i * 88

        if respondeu:
            if i == correta:
                cor_fundo = (0, 80, 0)
                cor_borda = VERDE
            elif i == selecionada:
                cor_fundo = (100, 0, 0)
                cor_borda = VERMELHO
            else:
                cor_fundo = (50, 50, 50)
                cor_borda = (80, 80, 80)
        else:
            cor_fundo = AZUL if i == selecionada else (50, 50, 50)
            cor_borda = AZUL_CLARO if i == selecionada else (80, 80, 80)

        pygame.draw.rect(tela, cor_fundo, (40, y, 720, 75), border_radius=8)
        pygame.draw.rect(tela, cor_borda, (40, y, 720, 75), width=2, border_radius=8)
        desenhar_texto(tela, f"{letra})  {opcao}", 18, BRANCO, 65, y + 26)

    # Mensagem de feedback
    if respondeu:
        msg = (
            "Correto!  ENTER para continuar"
            if acertou
            else "Errou!  ENTER para continuar"
        )
        cor_msg = VERDE if acertou else VERMELHO
        desenhar_texto(
            tela, msg, 17, cor_msg, LARGURA_TELA // 2, 510, centralizado=True
        )
    else:
        desenhar_texto(
            tela,
            "Setas UP/DOWN para navegar  |  ENTER para responder",
            14,
            AZUL_CLARO,
            LARGURA_TELA // 2,
            510,
            centralizado=True,
        )


def desenhar_resultado(
    tela, pontos, total_acertos, total_questoes, recorde, dificuldade
):
    # """Desenha a tela de resultado final com aproveitamento."""
    tela.fill(CINZA_ESCURO)

    aproveitamento = int((total_acertos / total_questoes) * 100)
    aprovado = aproveitamento >= 70

    desenhar_texto(
        tela, "Resultado Final", 42, AMARELO, LARGURA_TELA // 2, 60, centralizado=True
    )
    desenhar_texto(
        tela,
        f"Dificuldade: {dificuldade.capitalize()}",
        18,
        AZUL_CLARO,
        LARGURA_TELA // 2,
        120,
        centralizado=True,
    )

    desenhar_texto(
        tela,
        f"Acertos: {total_acertos} de {total_questoes}",
        26,
        BRANCO,
        LARGURA_TELA // 2,
        165,
        centralizado=True,
    )
    desenhar_texto(
        tela,
        f"Aproveitamento: {aproveitamento}%",
        24,
        BRANCO,
        LARGURA_TELA // 2,
        205,
        centralizado=True,
    )
    desenhar_texto(
        tela,
        f"Pontuacao: {pontos}",
        28,
        AMARELO,
        LARGURA_TELA // 2,
        250,
        centralizado=True,
    )
    desenhar_texto(
        tela,
        f"Recorde: {recorde}",
        20,
        AZUL_CLARO,
        LARGURA_TELA // 2,
        290,
        centralizado=True,
    )

    msg = "APROVADO! Parabens!" if aprovado else "Tente novamente!"
    cor = VERDE if aprovado else VERMELHO
    desenhar_texto(tela, msg, 30, cor, LARGURA_TELA // 2, 340, centralizado=True)

    desenhar_texto(
        tela,
        "ENTER para jogar novamente",
        18,
        AZUL_CLARO,
        LARGURA_TELA // 2,
        430,
        centralizado=True,
    )
    desenhar_texto(
        tela,
        "ESC para voltar ao menu",
        16,
        (150, 150, 150),
        LARGURA_TELA // 2,
        460,
        centralizado=True,
    )


def executar_jogo():
    """Executa o loop principal do PyQuiz."""
    pygame.init()

    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    relogio = pygame.time.Clock()
    pygame.display.set_caption(TITULO_JOGO)

    # Mapeamento de dificuldade
    nomes_dificuldade = ["facil", "medio", "dificil"]
    tempos_dificuldade = [TEMPO_FACIL, TEMPO_MEDIO, TEMPO_DIFICIL]

    # Carrega recorde salvo
    recorde = carregar_recorde(CAMINHO_RECORDE)

    # Estado do jogo
    estado = "menu"
    opcao_menu = 0
    dificuldade = "facil"
    tempo_questao = TEMPO_FACIL

    questoes = []
    indice_questao = 0
    opcao_resposta = 0
    respondeu = False
    acertou = False
    pontos = 0
    total_acertos = 0

    # Temporizador
    tempo_restante = tempo_questao
    ultimo_tick = 0

    rodando = True

    while rodando:
        relogio.tick(FPS)
        tempo_atual = pygame.time.get_ticks()

        # ── Temporizador (só conta durante a pergunta) ──
        if estado == "jogando" and not respondeu:
            if tempo_atual - ultimo_tick >= 1000:
                tempo_restante -= 1
                ultimo_tick = tempo_atual
                if tempo_restante <= 0:
                    # Tempo esgotado = erro
                    respondeu = True
                    acertou = False
                    opcao_resposta = -1

        # ── Eventos ─────────────────────────────────────
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

            if evento.type == pygame.KEYDOWN:
                # --- Menu ---
                if estado == "menu":
                    if evento.key == pygame.K_UP:
                        opcao_menu = limitar_valor(opcao_menu - 1, 0, 2)
                    if evento.key == pygame.K_DOWN:
                        opcao_menu = limitar_valor(opcao_menu + 1, 0, 2)
                    if evento.key == pygame.K_RETURN:
                        dificuldade = nomes_dificuldade[opcao_menu]
                        tempo_questao = tempos_dificuldade[opcao_menu]
                        questoes = carregar_questoes(CAMINHO_QUESTOES, dificuldade)
                        indice_questao = 0
                        opcao_resposta = 0
                        respondeu = False
                        pontos = 0
                        total_acertos = 0
                        tempo_restante = tempo_questao
                        ultimo_tick = pygame.time.get_ticks()
                        estado = "jogando"

                # --- Jogando ---
                elif estado == "jogando":
                    if not respondeu:
                        if evento.key == pygame.K_UP:
                            opcao_resposta = limitar_valor(opcao_resposta - 1, 0, 3)
                        if evento.key == pygame.K_DOWN:
                            opcao_resposta = limitar_valor(opcao_resposta + 1, 0, 3)
                        if evento.key == pygame.K_RETURN:
                            correta = questoes[indice_questao]["correta"]
                            acertou = opcao_resposta == correta
                            respondeu = True
                            if acertou:
                                bonus = tempo_restante
                                pontos = calcular_pontos(pontos, 10 + bonus)
                                total_acertos += 1
                    else:
                        if evento.key == pygame.K_RETURN:
                            indice_questao += 1
                            if indice_questao >= len(questoes):
                                # Fim do jogo
                                if pontos > recorde:
                                    recorde = pontos
                                    salvar_recorde(CAMINHO_RECORDE, recorde)
                                salvar_ranking(
                                    CAMINHO_RANKING, "Jogador", pontos, dificuldade
                                )
                                estado = "fim"
                            else:
                                opcao_resposta = 0
                                respondeu = False
                                acertou = False
                                tempo_restante = tempo_questao
                                ultimo_tick = pygame.time.get_ticks()

                # --- Fim ---
                elif estado == "fim":
                    if evento.key == pygame.K_RETURN:
                        dificuldade = nomes_dificuldade[opcao_menu]
                        tempo_questao = tempos_dificuldade[opcao_menu]
                        questoes = carregar_questoes(CAMINHO_QUESTOES, dificuldade)
                        indice_questao = 0
                        opcao_resposta = 0
                        respondeu = False
                        pontos = 0
                        total_acertos = 0
                        tempo_restante = tempo_questao
                        ultimo_tick = pygame.time.get_ticks()
                        estado = "jogando"

                # ESC sempre volta ao menu
                if evento.key == pygame.K_ESCAPE:
                    if estado == "menu":
                        rodando = False
                    else:
                        estado = "menu"
                        opcao_menu = 0

        # -------------Renderização ------------
        if estado == "menu":
            desenhar_menu(tela, opcao_menu)

        elif estado == "jogando":
            q = questoes[indice_questao]
            desenhar_pergunta(
                tela,
                indice_questao + 1,
                len(questoes),
                q["pergunta"],
                q["opcoes"],
                opcao_resposta,
                acertou,
                respondeu,
                q["correta"],
                tempo_restante,
                tempo_questao,
            )
            pygame.display.set_caption(
                f"{TITULO_JOGO} | Pontos: {pontos} | Recorde: {recorde}"
            )

        elif estado == "fim":
            desenhar_resultado(
                tela, pontos, total_acertos, len(questoes), recorde, dificuldade
            )

        pygame.display.flip()

    pygame.quit()

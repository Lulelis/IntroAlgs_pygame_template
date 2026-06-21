# src/jogo.py
# Loop principal do PyQuiz - Semana 4 (visual estilo dark/web)

import pygame

from src.config import (
    ALTURA_TELA,
    AMARELO,
    AMARELO_FUNDO,
    AZUL,
    AZUL_FUNDO,
    BORDA,
    CAMINHO_QUESTOES,
    CAMINHO_RANKING,
    CAMINHO_RECORDE,
    FPS,
    FUNDO,
    FUNDO_CARD,
    FUNDO_CARD_2,
    LARGURA_TELA,
    ROXO,
    TEMPO_DIFICIL,
    TEMPO_FACIL,
    TEMPO_MEDIO,
    TEXTO,
    TEXTO_FRACO,
    TITULO_JOGO,
    VERDE,
    VERDE_FUNDO,
    VERMELHO,
    VERMELHO_FUNDO,
)
from src.dados import (
    carregar_questoes,
    carregar_recorde,
    salvar_ranking,
    salvar_recorde,
)
from src.funcoes import (
    calcular_aproveitamento,
    calcular_pontos,
    jogador_aprovado,
    limitar_valor,
)
from src.ui import (
    anel_pontuacao,
    barra_progresso,
    bloco_codigo,
    caixa_arredondada,
    caixa_com_sombra,
    chip,
    cor_interpolada,
    desenhar_texto,
    desenhar_texto_quebrado,
    pulso,
)


# ── TELA: MENU (estilo cards do protótipo) ──────────────────
def desenhar_menu(tela, opcao_selecionada):
    tela.fill(FUNDO)
    ####
    # "logo" no topo, estilo terminal
    caixa_arredondada(
        tela, (LARGURA_TELA // 2 - 110, 30, 220, 34), FUNDO_CARD, BORDA, 1, raio=8
    )
    desenhar_texto(tela, ">_ python", 15, AZUL, LARGURA_TELA // 2 - 95, 39)
    desenhar_texto(tela, "quiz.py", 15, VERDE, LARGURA_TELA // 2 - 10, 39)

    desenhar_texto(
        tela,
        "Quiz de Python",
        34,
        TEXTO,
        LARGURA_TELA // 2,
        90,
        centralizado=True,
        negrito=True,
    )
    desenhar_texto(
        tela,
        "Escolha a dificuldade e teste seus conhecimentos",
        15,
        TEXTO_FRACO,
        LARGURA_TELA // 2,
        130,
        centralizado=True,
    )

    cards = [
        {
            "nome": "Facil",
            "desc": "Variaveis, tipos, loops",
            "tempo": TEMPO_FACIL,
            "cor": VERDE,
            "fundo": VERDE_FUNDO,
        },
        {
            "nome": "Medio",
            "desc": "Funcoes, listas, dicts",
            "tempo": TEMPO_MEDIO,
            "cor": AMARELO,
            "fundo": AMARELO_FUNDO,
        },
        {
            "nome": "Dificil",
            "desc": "OOP, erros, avancado",
            "tempo": TEMPO_DIFICIL,
            "cor": VERMELHO,
            "fundo": VERMELHO_FUNDO,
        },
    ]

    largura_card = 220
    altura_card = 150
    espaco = 20
    x_inicial = (LARGURA_TELA - (largura_card * 3 + espaco * 2)) // 2
    y_card = 175

    for i, card in enumerate(cards):
        x = x_inicial + i * (largura_card + espaco)
        selecionado = i == opcao_selecionada

        cor_fundo = FUNDO_CARD_2 if selecionado else FUNDO_CARD
        cor_borda = card["cor"] if selecionado else BORDA
        espessura = 2 if selecionado else 1

        caixa_com_sombra(tela, (x, y_card, largura_card, altura_card), cor_fundo, cor_borda, espessura, raio=14)

        desenhar_texto(
            tela,
            card["nome"],
            20,
            card["cor"],
            x + largura_card // 2,
            y_card + 25,
            centralizado=True,
            negrito=True,
        )
        desenhar_texto_quebrado(
            tela,
            card["desc"],
            13,
            TEXTO_FRACO,
            x + largura_card // 2,
            y_card + 60,
            largura_card - 30,
        )
        chip(
            tela,
            f"{card['tempo']}s por questao",
            x + 30,
            y_card + 105,
            card["cor"],
            card["fundo"],
            tamanho=12,
        )

    # Botão "iniciar"
    y_botao = y_card + altura_card + 35
    nome_sel = cards[opcao_selecionada]["nome"]
    caixa_arredondada(
        tela, (LARGURA_TELA // 2 - 150, y_botao, 300, 46), FUNDO_CARD, AZUL, 1, raio=10
    )
    desenhar_texto(
        tela,
        f"Iniciar - {nome_sel}",
        18,
        AZUL,
        LARGURA_TELA // 2,
        y_botao + 13,
        centralizado=True,
        negrito=True,
    )

    desenhar_texto(
        tela,
        "Setas ESQUERDA/DIREITA para navegar  |  ENTER para confirmar",
        13,
        TEXTO_FRACO,
        LARGURA_TELA // 2,
        y_botao + 70,
        centralizado=True,
    )
    desenhar_texto(
        tela,
        "ESC para sair",
        12,
        (90, 90, 105),
        LARGURA_TELA // 2,
        y_botao + 92,
        centralizado=True,
    )


# ── TELA: PERGUNTA ───────────────────────────────────────────
def desenhar_pergunta(
    tela,
    numero,
    total,
    questao,
    selecionada,
    acertou,
    respondeu,
    tempo_restante,
    tempo_total,
    pontos,
    dificuldade_info,
):
    tela.fill(FUNDO)
    cor_dif, fundo_dif, nome_dif = dificuldade_info

    margem = 40
    largura_conteudo = LARGURA_TELA - margem * 2

    # Cabeçalho: contador + placar
    desenhar_texto(tela, f"Questao {numero} de {total}", 14, TEXTO_FRACO, margem, 20)
    caixa_arredondada(
        tela, (LARGURA_TELA - margem - 90, 14, 90, 26), VERDE_FUNDO, VERDE, 1, raio=13
    )
    desenhar_texto(
        tela,
        f"{pontos} pts",
        13,
        VERDE,
        LARGURA_TELA - margem - 45,
        20,
        centralizado=True,
        negrito=True,
    )

    # Barra de progresso (questões)
    barra_progresso(
        tela, margem, 50, largura_conteudo, 6, numero / total, FUNDO_CARD, AZUL, raio=3
    )

    # Chip de dificuldade + temporizador
    chip(tela, nome_dif, margem, 68, cor_dif, fundo_dif, tamanho=12)

    cor_tempo = (
        VERDE
        if tempo_restante > tempo_total * 0.5
        else AMARELO
        if tempo_restante > tempo_total * 0.25
        else VERMELHO
    )
    fundo_tempo = (
        VERDE_FUNDO
        if tempo_restante > tempo_total * 0.5
        else AMARELO_FUNDO
        if tempo_restante > tempo_total * 0.25
        else VERMELHO_FUNDO
    )

    # Efeito pulsante quando o tempo esta acabando (urgencia)
    if tempo_restante <= tempo_total * 0.25 and tempo_restante > 0:
        fator = pulso(velocidade=5)
        cor_tempo = cor_interpolada(VERMELHO, (255, 255, 255), fator * 0.4)

    chip(
        tela,
        f"{tempo_restante}s",
        LARGURA_TELA - margem - 60,
        68,
        cor_tempo,
        fundo_tempo,
        tamanho=12,
    )

    y = 110

    # Pergunta
    desenhar_texto_quebrado(
        tela,
        questao["pergunta"],
        19,
        TEXTO,
        LARGURA_TELA // 2,
        y,
        largura_conteudo - 20,
        espacamento=26,
    )
    y += 55 if len(questao["pergunta"]) < 55 else 80

    # Bloco de código (se houver)
    if questao.get("codigo"):
        bloco_codigo(
            tela,
            questao["codigo"],
            margem,
            y,
            largura_conteudo,
            (11, 11, 18),
            AZUL,
            TEXTO,
            tamanho=15,
        )
        num_linhas = len(questao["codigo"].split("\n"))
        y += (15 + 8) * num_linhas + 20 + 15

    # Alternativas
    letras = ["A", "B", "C", "D"]
    altura_opt = 50
    espaco_opt = 10

    for i, (letra, opcao) in enumerate(zip(letras, questao["opcoes"])):
        rect = (margem, y, largura_conteudo, altura_opt)

        if respondeu:
            if i == questao["correta"]:
                cor_fundo, cor_borda, cor_txt = VERDE_FUNDO, VERDE, VERDE
            elif i == selecionada:
                cor_fundo, cor_borda, cor_txt = VERMELHO_FUNDO, VERMELHO, VERMELHO
            else:
                cor_fundo, cor_borda, cor_txt = FUNDO_CARD, BORDA, TEXTO_FRACO
        else:
            if i == selecionada:
                cor_fundo, cor_borda, cor_txt = FUNDO_CARD_2, AZUL, TEXTO
            else:
                cor_fundo, cor_borda, cor_txt = FUNDO_CARD, BORDA, TEXTO

        caixa_arredondada(
            tela,
            rect,
            cor_fundo,
            cor_borda,
            2 if (i == selecionada or (respondeu and i == questao["correta"])) else 1,
            raio=10,
        )

        # "letra" estilo badge
        caixa_arredondada(
            tela,
            (margem + 10, y + 13, 24, 24),
            FUNDO_CARD_2 if not respondeu else cor_borda,
            raio=5,
        )
        cor_letra = (
            TEXTO_FRACO
            if not respondeu
            else (FUNDO if i in (selecionada, questao["correta"]) else TEXTO_FRACO)
        )
        desenhar_texto(
            tela,
            letra,
            12,
            cor_letra,
            margem + 22,
            y + 19,
            centralizado=True,
            negrito=True,
        )

        desenhar_texto(tela, opcao, 15, cor_txt, margem + 48, y + 17)

        y += altura_opt + espaco_opt

    # Feedback final
    y += 8
    if respondeu:
        if acertou:
            desenhar_texto(
                tela,
                "Correto!  Pressione ENTER para continuar",
                14,
                VERDE,
                LARGURA_TELA // 2,
                y,
                centralizado=True,
                negrito=True,
            )
        else:
            desenhar_texto(
                tela,
                "Incorreto.  Pressione ENTER para continuar",
                14,
                VERMELHO,
                LARGURA_TELA // 2,
                y,
                centralizado=True,
                negrito=True,
            )
        if questao.get("explicacao"):
            desenhar_texto_quebrado(
                tela,
                questao["explicacao"],
                12,
                TEXTO_FRACO,
                LARGURA_TELA // 2,
                y + 22,
                largura_conteudo - 40,
                espacamento=18,
            )
    else:
        desenhar_texto(
            tela,
            "Setas CIMA/BAIXO para escolher  |  ENTER para responder",
            12,
            TEXTO_FRACO,
            LARGURA_TELA // 2,
            y,
            centralizado=True,
        )


# ── TELA: RESULTADO ──────────────────────────────────────────
def desenhar_resultado(
    tela,
    pontos,
    total_acertos,
    total_questoes,
    recorde,
    dificuldade_info,
    opcao_selecionada,
):
    tela.fill(FUNDO)
    cor_dif, fundo_dif, nome_dif = dificuldade_info

    aproveitamento = calcular_aproveitamento(total_acertos, total_questoes)
    aprovado = jogador_aprovado(total_acertos, total_questoes)

    cor_anel = VERDE if aprovado else (AMARELO if aproveitamento >= 40 else VERMELHO)
    fundo_anel = (
        VERDE_FUNDO
        if aprovado
        else (AMARELO_FUNDO if aproveitamento >= 40 else VERMELHO_FUNDO)
    )

    centro_x = LARGURA_TELA // 2

    anel_pontuacao(
        tela,
        centro_x,
        130,
        64,
        f"{total_acertos}/{total_questoes}",
        "acertos",
        cor_anel,
        fundo_anel,
    )

    titulo = "Excelente!" if aprovado else "Continue praticando!"
    desenhar_texto(
        tela, titulo, 24, TEXTO, centro_x, 215, centralizado=True, negrito=True
    )
    desenhar_texto(
        tela,
        f"Aproveitamento de {aproveitamento}%",
        14,
        TEXTO_FRACO,
        centro_x,
        248,
        centralizado=True,
    )

    chip(tela, nome_dif, centro_x - 35, 278, cor_dif, fundo_dif, tamanho=12)

    # Cards de estatística
    y_cards = 330
    largura_card = 220
    espaco = 20
    x_inicial = (LARGURA_TELA - (largura_card * 2 + espaco)) // 2

    caixa_com_sombra(
        tela, (x_inicial, y_cards, largura_card, 80), FUNDO_CARD, BORDA, 1, raio=12
    )
    desenhar_texto(
        tela,
        "Pontuacao",
        12,
        TEXTO_FRACO,
        x_inicial + largura_card // 2,
        y_cards + 16,
        centralizado=True,
    )
    desenhar_texto(
        tela,
        str(pontos),
        28,
        AZUL,
        x_inicial + largura_card // 2,
        y_cards + 36,
        centralizado=True,
        negrito=True,
    )

    x2 = x_inicial + largura_card + espaco
    caixa_com_sombra(
        tela, (x2, y_cards, largura_card, 80), FUNDO_CARD, BORDA, 1, raio=12
    )
    desenhar_texto(
        tela,
        "Recorde",
        12,
        TEXTO_FRACO,
        x2 + largura_card // 2,
        y_cards + 16,
        centralizado=True,
    )
    desenhar_texto(
        tela,
        str(recorde),
        28,
        ROXO,
        x2 + largura_card // 2,
        y_cards + 36,
        centralizado=True,
        negrito=True,
    )

    # Botões
    # Botões (destaca o selecionado)
    y_botoes = y_cards + 110

    if opcao_selecionada == 0:
        caixa_arredondada(
            tela, (x_inicial, y_botoes, largura_card, 46), AZUL_FUNDO, AZUL, 2, raio=10
        )
        desenhar_texto(
            tela,
            "Jogar de novo",
            15,
            AZUL,
            x_inicial + largura_card // 2,
            y_botoes + 14,
            centralizado=True,
            negrito=True,
        )
    else:
        caixa_arredondada(
            tela, (x_inicial, y_botoes, largura_card, 46), FUNDO_CARD, BORDA, 1, raio=10
        )
        desenhar_texto(
            tela,
            "Jogar de novo",
            15,
            TEXTO_FRACO,
            x_inicial + largura_card // 2,
            y_botoes + 14,
            centralizado=True,
        )

    if opcao_selecionada == 1:
        caixa_arredondada(
            tela, (x2, y_botoes, largura_card, 46), FUNDO_CARD_2, AZUL, 2, raio=10
        )
        desenhar_texto(
            tela,
            "Voltar ao menu",
            15,
            TEXTO,
            x2 + largura_card // 2,
            y_botoes + 14,
            centralizado=True,
            negrito=True,
        )
    else:
        caixa_arredondada(
            tela, (x2, y_botoes, largura_card, 46), FUNDO_CARD, BORDA, 1, raio=10
        )
        desenhar_texto(
            tela,
            "Voltar ao menu",
            15,
            TEXTO_FRACO,
            x2 + largura_card // 2,
            y_botoes + 14,
            centralizado=True,
        )

    desenhar_texto(
        tela,
        "Setas para escolher  |  ENTER para confirmar",
        12,
        TEXTO_FRACO,
        centro_x,
        y_botoes + 70,
        centralizado=True,
    )


# ── LOOP PRINCIPAL ───────────────────────────────────────────
def executar_jogo():
    """Executa o loop principal do PyQuiz."""
    pygame.init()

    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    relogio = pygame.time.Clock()
    pygame.display.set_caption(TITULO_JOGO)

    nomes_dificuldade = ["facil", "medio", "dificil"]
    tempos_dificuldade = [TEMPO_FACIL, TEMPO_MEDIO, TEMPO_DIFICIL]
    cores_dificuldade = [VERDE, AMARELO, VERMELHO]
    fundos_dificuldade = [VERDE_FUNDO, AMARELO_FUNDO, VERMELHO_FUNDO]
    labels_dificuldade = ["Facil", "Medio", "Dificil"]

    recorde = carregar_recorde(CAMINHO_RECORDE)

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

    tempo_restante = tempo_questao
    ultimo_tick = 0
    opcao_fim = 0

    rodando = True

    def iniciar_partida():
        nonlocal dificuldade, tempo_questao, questoes, indice_questao
        nonlocal opcao_resposta, respondeu, pontos, total_acertos
        nonlocal tempo_restante, ultimo_tick, estado, acertou, opcao_fim

        dificuldade = nomes_dificuldade[opcao_menu]
        tempo_questao = tempos_dificuldade[opcao_menu]
        questoes = carregar_questoes(CAMINHO_QUESTOES, dificuldade)
        indice_questao = 0
        opcao_resposta = 0
        respondeu = False
        acertou = False
        pontos = 0
        total_acertos = 0
        tempo_restante = tempo_questao
        ultimo_tick = pygame.time.get_ticks()
        estado = "jogando"
        opcao_fim = 0

    while rodando:
        relogio.tick(FPS)
        tempo_atual = pygame.time.get_ticks()

        if estado == "jogando" and not respondeu:
            if tempo_atual - ultimo_tick >= 1000:
                tempo_restante -= 1
                ultimo_tick = tempo_atual
                if tempo_restante <= 0:
                    respondeu = True
                    acertou = False
                    opcao_resposta = -1

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

            if evento.type == pygame.KEYDOWN:
                if estado == "menu":
                    if evento.key in (pygame.K_LEFT, pygame.K_UP):
                        opcao_menu = limitar_valor(opcao_menu - 1, 0, 2)
                    if evento.key in (pygame.K_RIGHT, pygame.K_DOWN):
                        opcao_menu = limitar_valor(opcao_menu + 1, 0, 2)
                    if evento.key == pygame.K_RETURN:
                        iniciar_partida()

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
                                pontos = calcular_pontos(pontos, 10 + tempo_restante)
                                total_acertos += 1
                    else:
                        if evento.key == pygame.K_RETURN:
                            indice_questao += 1
                            if indice_questao >= len(questoes):
                                if pontos > recorde:
                                    recorde = pontos
                                    salvar_recorde(CAMINHO_RECORDE, recorde)
                                salvar_ranking(
                                    CAMINHO_RANKING, "Jogador", pontos, dificuldade
                                )
                                estado = "fim"
                                opcao_fim = 0
                            else:
                                opcao_resposta = 0
                                respondeu = False
                                acertou = False
                                tempo_restante = tempo_questao
                                ultimo_tick = pygame.time.get_ticks()

                elif estado == "fim":
                    if evento.key in (
                        pygame.K_LEFT,
                        pygame.K_RIGHT,
                        pygame.K_UP,
                        pygame.K_DOWN,
                    ):
                        opcao_fim = 1 - opcao_fim
                    if evento.key == pygame.K_RETURN:
                        if opcao_fim == 0:
                            iniciar_partida()
                        else:
                            estado = "menu"
                            opcao_menu = 0

                if evento.key == pygame.K_ESCAPE:
                    if estado == "menu":
                        rodando = False
                    else:
                        estado = "menu"
                        opcao_menu = 0

        # ── Renderização ──
        if estado == "menu":
            desenhar_menu(tela, opcao_menu)

        elif estado == "jogando":
            idx = nomes_dificuldade.index(dificuldade)
            info_dif = (
                cores_dificuldade[idx],
                fundos_dificuldade[idx],
                labels_dificuldade[idx],
            )
            desenhar_pergunta(
                tela,
                indice_questao + 1,
                len(questoes),
                questoes[indice_questao],
                opcao_resposta,
                acertou,
                respondeu,
                tempo_restante,
                tempo_questao,
                pontos,
                info_dif,
            )
            pygame.display.set_caption(
                f"{TITULO_JOGO} | Pontos: {pontos} | Recorde: {recorde}"
            )

        elif estado == "fim":
            idx = nomes_dificuldade.index(dificuldade)
            info_dif = (
                cores_dificuldade[idx],
                fundos_dificuldade[idx],
                labels_dificuldade[idx],
            )
            desenhar_resultado(
                tela, pontos, total_acertos, len(questoes), recorde, info_dif, opcao_fim
            )

        pygame.display.flip()

    pygame.quit()

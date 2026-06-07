# src/jogo.py
# Loop principal do PyQuiz - Protótipo Semana 2

import pygame

from src.config import (
    ALTURA_TELA,
    AMARELO,
    AZUL,
    AZUL_CLARO,
    BRANCO,
    BRANCO_GELO,
    CAMINHO_RECORDE,
    CINZA_ESCURO,
    FPS,
    LARGURA_TELA,
    TITULO_JOGO,
    VERDE,
    VERMELHO,
)
from src.dados import (
    carregar_recorde,
    salvar_recorde,
)
from src.funcoes import (
    calcular_pontos,
    limitar_valor,
)


def desenhar_texto(tela, texto, tamanho, cor, x, y, centralizado=False):
    ### Renderiza texto na tela usando Pygame
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
    #### Desenha a tela inicial do menu com as opções de dificuldade
    tela.fill(CINZA_ESCURO)

    desenhar_texto(
        tela, "PyQuiz", 64, AMARELO, LARGURA_TELA // 2, 80, centralizado=True
    )
    desenhar_texto(
        tela,
        "Quiz de Python",
        24,
        AZUL_CLARO,
        LARGURA_TELA // 2,
        155,
        centralizado=True,
    )
    desenhar_texto(
        tela,
        "Escolha a dificuldade:",
        20,
        BRANCO,
        LARGURA_TELA // 2,
        220,
        centralizado=True,
    )

    opcoes = ["Facil", "Medio", "Dificil"]
    cores_opcao = [VERDE, AMARELO, VERMELHO]

    for i, (nome, cor) in enumerate(zip(opcoes, cores_opcao)):
        y = 280 + i * 70
        cor_fundo = AZUL if i == opcao_selecionada else (60, 60, 60)
        pygame.draw.rect(tela, cor_fundo, (250, y, 300, 50), border_radius=10)
        pygame.draw.rect(tela, cor, (250, y, 300, 50), width=2, border_radius=10)
        desenhar_texto(
            tela, nome, 28, cor, LARGURA_TELA // 2, y + 10, centralizado=True
        )

    desenhar_texto(
        tela,
        "Use as setas UP/DOWN para navegar",
        16,
        AZUL_CLARO,
        LARGURA_TELA // 2,
        510,
        centralizado=True,
    )
    desenhar_texto(
        tela,
        "Pressione ENTER para confirmar",
        16,
        AZUL_CLARO,
        LARGURA_TELA // 2,
        535,
        centralizado=True,
    )


def desenhar_pergunta(
    tela, numero, total, pergunta, opcoes, selecionada, acertou, respondeu, correta
):
    """Desenha a pergunta atual e suas alternativas na tela."""
    tela.fill(CINZA_ESCURO)

    ### Cabeçalho
    desenhar_texto(tela, f"Questao {numero} de {total}", 20, AZUL_CLARO, 20, 15)

    #### Barra de progresso usando limitar_valor do template
    progresso = limitar_valor(numero, 1, total)
    largura_barra = int((progresso / total) * (LARGURA_TELA - 40))
    pygame.draw.rect(
        tela, (60, 60, 60), (20, 45, LARGURA_TELA - 40, 10), border_radius=5
    )
    pygame.draw.rect(tela, AZUL, (20, 45, largura_barra, 10), border_radius=5)

    # Pergunta
    desenhar_texto(
        tela, pergunta, 22, BRANCO_GELO, LARGURA_TELA // 2, 80, centralizado=True
    )

    ### Alternativas
    letras = ["A", "B", "C", "D"]
    for i, (letra, opcao) in enumerate(zip(letras, opcoes)):
        y = 200 + i * 75

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

        pygame.draw.rect(tela, cor_fundo, (60, y, 680, 55), border_radius=8)
        pygame.draw.rect(tela, cor_borda, (60, y, 680, 55), width=2, border_radius=8)
        desenhar_texto(tela, f"{letra})  {opcao}", 20, BRANCO, 90, y + 16)

    if respondeu:
        msg = (
            "Correto! Pressione ENTER para continuar"
            if acertou
            else "Errou! Pressione ENTER para continuar"
        )
        cor_msg = VERDE if acertou else VERMELHO
        desenhar_texto(
            tela, msg, 18, cor_msg, LARGURA_TELA // 2, 520, centralizado=True
        )
    else:
        desenhar_texto(
            tela,
            "Setas UP/DOWN para navegar | ENTER para responder",
            15,
            AZUL_CLARO,
            LARGURA_TELA // 2,
            530,
            centralizado=True,
        )


def desenhar_resultado(tela, pontos, acertou, recorde):
    """Desenha a tela de resultado final."""
    tela.fill(CINZA_ESCURO)
    desenhar_texto(
        tela, "Resultado", 48, AMARELO, LARGURA_TELA // 2, 160, centralizado=True
    )
    desenhar_texto(
        tela, f"Pontos: {pontos}", 32, BRANCO, LARGURA_TELA // 2, 250, centralizado=True
    )
    desenhar_texto(
        tela,
        f"Recorde: {recorde}",
        22,
        AZUL_CLARO,
        LARGURA_TELA // 2,
        300,
        centralizado=True,
    )
    resultado = "Voce acertou!" if acertou else "Voce errou!"
    cor = VERDE if acertou else VERMELHO
    desenhar_texto(tela, resultado, 28, cor, LARGURA_TELA // 2, 350, centralizado=True)
    desenhar_texto(
        tela,
        "ENTER para jogar novamente",
        18,
        AZUL_CLARO,
        LARGURA_TELA // 2,
        440,
        centralizado=True,
    )
    desenhar_texto(
        tela,
        "ESC para sair",
        16,
        (150, 150, 150),
        LARGURA_TELA // 2,
        470,
        centralizado=True,
    )


def executar_jogo():
    ### Executa o loop principal do PyQuiz
    pygame.init()

    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    relogio = pygame.time.Clock()
    pygame.display.set_caption(TITULO_JOGO)

    #### Questão de teste (Semana 2- apenas um protótipo))
    pergunta_teste = "Qual e o tipo de dado do valor 42 em Python?"
    opcoes_teste = ["int", "float", "str", "bool"]
    correta_teste = 0

    ### --- Carrega recorde do arquivo usando dados.py do template ---
    recorde = carregar_recorde(CAMINHO_RECORDE)

    #### --- Estado
    estado = "menu"
    opcao_menu = 0
    opcao_resposta = 0
    respondeu = False
    acertou = False
    pontos = 0
    rodando = True

    while rodando:
        relogio.tick(FPS)

        ### Eventos:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

            if evento.type == pygame.KEYDOWN:
                if estado == "menu":
                    if evento.key == pygame.K_UP:
                        opcao_menu = limitar_valor(opcao_menu - 1, 0, 2)
                    if evento.key == pygame.K_DOWN:
                        opcao_menu = limitar_valor(opcao_menu + 1, 0, 2)
                    if evento.key == pygame.K_RETURN:
                        estado = "jogando"
                        opcao_resposta = 0
                        respondeu = False

                elif estado == "jogando":
                    if not respondeu:
                        if evento.key == pygame.K_UP:
                            opcao_resposta = limitar_valor(opcao_resposta - 1, 0, 3)
                        if evento.key == pygame.K_DOWN:
                            opcao_resposta = limitar_valor(opcao_resposta + 1, 0, 3)
                        if evento.key == pygame.K_RETURN:
                            respondeu = True
                            acertou = opcao_resposta == correta_teste
                            # Usa calcular_pontos do template
                            if acertou:
                                pontos = calcular_pontos(pontos, 10)
                    else:
                        if evento.key == pygame.K_RETURN:
                            # Salva recorde usando dados.py do template
                            if pontos > recorde:
                                recorde = pontos
                                salvar_recorde(CAMINHO_RECORDE, recorde)
                            estado = "fim"

                elif estado == "fim":
                    if evento.key == pygame.K_RETURN:
                        estado = "menu"
                        opcao_menu = 0
                        opcao_resposta = 0
                        respondeu = False
                        acertou = False
                        pontos = 0

                if evento.key == pygame.K_ESCAPE:
                    if estado == "menu":
                        rodando = False
                    else:
                        estado = "menu"

        ### - Renderização:
        if estado == "menu":
            desenhar_menu(tela, opcao_menu)

        elif estado == "jogando":
            desenhar_pergunta(
                tela,
                1,
                1,
                pergunta_teste,
                opcoes_teste,
                opcao_resposta,
                acertou,
                respondeu,
                correta_teste,
            )
            pygame.display.set_caption(
                f"{TITULO_JOGO} | Pontos: {pontos} | Recorde: {recorde}"
            )

        elif estado == "fim":
            desenhar_resultado(tela, pontos, acertou, recorde)

        pygame.display.flip()

    pygame.quit()

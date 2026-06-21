# src/ui.py
# Funções de interface visual do PyQuiz (estilo dark moderno)

import math

import pygame

_FONTE_CACHE = {}


def fonte(tamanho, negrito=False):
    """Retorna uma fonte cacheada para evitar recriação a cada frame."""
    chave = (tamanho, negrito)
    if chave not in _FONTE_CACHE:
        _FONTE_CACHE[chave] = pygame.font.SysFont("segoeui", tamanho, bold=negrito)
    return _FONTE_CACHE[chave]


def desenhar_texto(tela, texto, tamanho, cor, x, y, centralizado=False, negrito=False):
    """Renderiza texto na tela na posição indicada."""
    fnt = fonte(tamanho, negrito)
    superficie = fnt.render(texto, True, cor)
    rect = superficie.get_rect()
    if centralizado:
        rect.centerx = x
    else:
        rect.x = x
    rect.y = y
    tela.blit(superficie, rect)
    return rect


def desenhar_texto_quebrado(
    tela, texto, tamanho, cor, x, y, largura_max, centralizado=True, espacamento=26
):
    """Quebra o texto em múltiplas linhas para caber na largura máxima."""
    fnt = fonte(tamanho)
    palavras = texto.split(" ")
    linhas = []
    linha_atual = ""

    for palavra in palavras:
        teste = (linha_atual + " " + palavra).strip()
        if fnt.size(teste)[0] <= largura_max:
            linha_atual = teste
        else:
            linhas.append(linha_atual)
            linha_atual = palavra
    if linha_atual:
        linhas.append(linha_atual)

    for i, linha in enumerate(linhas):
        desenhar_texto(
            tela, linha, tamanho, cor, x, y + i * espacamento, centralizado=centralizado
        )

    return len(linhas)


def caixa_arredondada(
    tela, rect, cor_fundo, cor_borda=None, espessura_borda=0, raio=12
):
    """Desenha um retângulo com cantos arredondados (card moderno)."""
    pygame.draw.rect(tela, cor_fundo, rect, border_radius=raio)
    if cor_borda and espessura_borda > 0:
        pygame.draw.rect(
            tela, cor_borda, rect, width=espessura_borda, border_radius=raio
        )


def barra_progresso(
    tela, x, y, largura, altura, progresso, cor_fundo, cor_barra, raio=6
):
    """Desenha uma barra de progresso (0.0 a 1.0)."""
    progresso = max(0.0, min(1.0, progresso))
    caixa_arredondada(tela, (x, y, largura, altura), cor_fundo, raio=raio)
    largura_preenchida = int(largura * progresso)
    if largura_preenchida > 0:
        caixa_arredondada(
            tela, (x, y, largura_preenchida, altura), cor_barra, raio=raio
        )


def chip(
    tela, texto, x, y, cor_texto, cor_fundo, tamanho=14, padding_x=12, padding_y=5
):
    """Desenha uma 'tag' pequena tipo as do protótipo web (ex: Facil, Topico)."""
    fnt = fonte(tamanho, negrito=True)
    superficie = fnt.render(texto, True, cor_texto)
    largura = superficie.get_width() + padding_x * 2
    altura = superficie.get_height() + padding_y * 2
    rect = pygame.Rect(x, y, largura, altura)
    caixa_arredondada(tela, rect, cor_fundo, raio=altura // 2)
    tela.blit(superficie, (x + padding_x, y + padding_y))
    return rect


def bloco_codigo(
    tela, codigo, x, y, largura, cor_fundo, cor_borda, cor_texto, tamanho=16
):
    """Desenha um bloco de código com fundo escuro e fonte monoespaçada (estilo terminal)."""
    fnt = pygame.font.SysFont("consolas", tamanho)
    linhas = codigo.split("\n")
    altura_linha = tamanho + 8
    altura_total = altura_linha * len(linhas) + 20

    rect = pygame.Rect(x, y, largura, altura_total)
    caixa_arredondada(tela, rect, cor_fundo, cor_borda, espessura_borda=1, raio=8)

    # barra lateral azul (igual ao protótipo)
    pygame.draw.rect(tela, cor_borda, (x, y, 4, altura_total), border_radius=2)

    for i, linha in enumerate(linhas):
        superficie = fnt.render(linha, True, cor_texto)
        tela.blit(superficie, (x + 16, y + 10 + i * altura_linha))

    return rect


def anel_pontuacao(
    tela, centro_x, centro_y, raio, valor_texto, label_texto, cor_anel, cor_fundo
):
    """Desenha o 'anel de pontuação' circular igual ao da tela de resultado web."""
    pygame.draw.circle(tela, cor_fundo, (centro_x, centro_y), raio)
    pygame.draw.circle(tela, cor_anel, (centro_x, centro_y), raio, width=3)

    desenhar_texto(
        tela,
        valor_texto,
        30,
        cor_anel,
        centro_x,
        centro_y - 22,
        centralizado=True,
        negrito=True,
    )
    desenhar_texto(
        tela,
        label_texto,
        13,
        (150, 150, 160),
        centro_x,
        centro_y + 12,
        centralizado=True,
    )


def sombra_caixa(tela, rect, raio=12, intensidade=40):
    """Desenha uma sombra sutil por baixo de um card (efeito de profundidade)."""
    x, y, largura, altura = rect
    sombra_surf = pygame.Surface((largura + 8, altura + 8), pygame.SRCALPHA)
    pygame.draw.rect(
        sombra_surf, (0, 0, 0, intensidade), (4, 6, largura, altura), border_radius=raio
    )
    tela.blit(sombra_surf, (x - 4, y - 2))


def caixa_com_sombra(tela, rect, cor_fundo, cor_borda=None, espessura_borda=0, raio=12):
    """Card com sombra sutil por baixo, estilo material design."""
    sombra_caixa(tela, rect, raio=raio)
    caixa_arredondada(tela, rect, cor_fundo, cor_borda, espessura_borda, raio)


def pulso(velocidade=4):
    """Retorna um valor entre 0.0 e 1.0 que oscila com o tempo (efeito pulsante)."""
    return (math.sin(pygame.time.get_ticks() / 1000 * velocidade) + 1) / 2


def cor_interpolada(cor_a, cor_b, fator):
    """Mistura duas cores RGB de acordo com um fator de 0.0 a 1.0."""
    fator = max(0.0, min(1.0, fator))
    return tuple(int(a + (b - a) * fator) for a, b in zip(cor_a, cor_b))


def linha_divisoria(tela, x, y, largura, cor, espessura=1):
    """Desenha uma linha horizontal sutil (separador visual)."""
    pygame.draw.rect(tela, cor, (x, y, largura, espessura))

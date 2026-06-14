# tests/test_logica.py
# Testes das funções auxiliares do PyQuiz

from src.funcoes import (
    calcular_aproveitamento,
    calcular_bonus_tempo,
    calcular_pontos,
    jogador_aprovado,
    jogador_perdeu,
    limitar_valor,
    resposta_correta,
)


# ── calcular_pontos ──────────────────────────────────────
def test_calcular_pontos_basico():
    assert calcular_pontos(0, 10) == 10


def test_calcular_pontos_acumulado():
    assert calcular_pontos(20, 15) == 35


def test_calcular_pontos_zero():
    assert calcular_pontos(0, 0) == 0


# ── limitar_valor ────────────────────────────────────────
def test_limitar_valor_dentro():
    assert limitar_valor(2, 0, 3) == 2


def test_limitar_valor_abaixo():
    assert limitar_valor(-1, 0, 3) == 0


def test_limitar_valor_acima():
    assert limitar_valor(5, 0, 3) == 3


# ── jogador_perdeu ───────────────────────────────────────
def test_jogador_perdeu_sem_vidas():
    assert jogador_perdeu(0) == True


def test_jogador_perdeu_com_vidas():
    assert jogador_perdeu(3) == False


def test_jogador_perdeu_negativo():
    assert jogador_perdeu(-1) == True


# ── calcular_aproveitamento ──────────────────────────────
def test_aproveitamento_total():
    assert calcular_aproveitamento(15, 15) == 100


def test_aproveitamento_metade():
    assert calcular_aproveitamento(7, 15) == 46


def test_aproveitamento_zero():
    assert calcular_aproveitamento(0, 15) == 0


def test_aproveitamento_sem_questoes():
    assert calcular_aproveitamento(0, 0) == 0


# ── jogador_aprovado ─────────────────────────────────────
def test_aprovado_acima_minimo():
    assert jogador_aprovado(11, 15) == True


def test_aprovado_abaixo_minimo():
    assert jogador_aprovado(5, 15) == False


def test_aprovado_exatamente_70():
    assert jogador_aprovado(10, 15) == False  # 66% < 70%


def test_aprovado_minimo_customizado():
    assert jogador_aprovado(5, 10, minimo=50) == True


# ── calcular_bonus_tempo ─────────────────────────────────
def test_bonus_tempo_normal():
    assert calcular_bonus_tempo(15) == 15


def test_bonus_tempo_zero():
    assert calcular_bonus_tempo(0) == 0


def test_bonus_tempo_negativo():
    assert calcular_bonus_tempo(-5) == 0


# ── resposta_correta ─────────────────────────────────────
def test_resposta_correta_acerto():
    assert resposta_correta(0, 0) == True


def test_resposta_correta_erro():
    assert resposta_correta(2, 0) == False


def test_resposta_correta_ultima():
    assert resposta_correta(3, 3) == True

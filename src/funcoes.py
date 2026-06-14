# src/funcoes.py
# Funções auxiliares do PyQuiz


def calcular_pontos(pontos_atual, pontos_ganhos):
    """Soma os pontos ganhos à pontuação atual."""
    return pontos_atual + pontos_ganhos


def tomar_dano(vida_atual, dano):
    """Reduz a vida atual com base no dano recebido."""
    return vida_atual - dano


def jogador_perdeu(vidas):
    """Indica se o jogador ficou sem vidas."""
    return vidas <= 0


def limitar_valor(valor, minimo, maximo):
    """Mantém um valor dentro do intervalo [minimo, maximo]."""
    if valor < minimo:
        return minimo
    if valor > maximo:
        return maximo
    return valor


def verificar_colisao(retangulo_1, retangulo_2):
    """Verifica sobreposição entre dois retângulos do Pygame."""
    return retangulo_1.colliderect(retangulo_2)


def calcular_aproveitamento(total_acertos, total_questoes):
    """Retorna o aproveitamento percentual do jogador."""
    if total_questoes == 0:
        return 0
    return int((total_acertos / total_questoes) * 100)


def jogador_aprovado(total_acertos, total_questoes, minimo=70):
    """Retorna True se o aproveitamento for maior ou igual ao mínimo."""
    return calcular_aproveitamento(total_acertos, total_questoes) >= minimo


def calcular_bonus_tempo(tempo_restante):
    """Retorna pontos bônus com base no tempo restante."""
    return max(0, tempo_restante)


def resposta_correta(opcao_escolhida, indice_correto):
    """Verifica se a opção escolhida é a correta."""
    return opcao_escolhida == indice_correto

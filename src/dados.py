# src/dados.py
# Funções de leitura e escrita de arquivos do PyQuiz
import json
import random


def salvar_recorde(caminho_arquivo, pontuacao):
    """Salva a pontuação recorde em arquivo texto."""
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(str(pontuacao))


def carregar_recorde(caminho_arquivo):
    """Carrega o recorde salvo; retorna 0 se não existir valor válido."""
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read().strip()
            if conteudo == "":
                return 0
            return int(conteudo)
    except FileNotFoundError:
        return 0


def carregar_questoes(caminho_arquivo, dificuldade):
    """Carrega e embaralha as questões do JSON pela dificuldade escolhida."""
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
        questoes = dados[dificuldade]
        random.shuffle(questoes)
        return questoes
    except FileNotFoundError:
        return []
    except KeyError:
        return []


def salvar_ranking(caminho_arquivo, nome, pontos, dificuldade):
    """Salva o resultado da partida no arquivo de ranking."""
    with open(caminho_arquivo, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome};{pontos};{dificuldade}\n")


def carregar_ranking(caminho_arquivo):
    """Carrega o ranking do arquivo e retorna uma lista de dicionários."""
    ranking = []
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                partes = linha.strip().split(";")
                if len(partes) == 3:
                    ranking.append(
                        {
                            "nome": partes[0],
                            "pontos": int(partes[1]),
                            "dificuldade": partes[2],
                        }
                    )
    except FileNotFoundError:
        return []
    ranking.sort(key=lambda x: x["pontos"], reverse=True)
    return ranking

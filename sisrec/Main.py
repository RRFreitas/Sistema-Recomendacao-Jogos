from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from json import load, dump
from models.Jogo import Jogo
from models.Similaridade import Similaridade
import VectorSpaceModel

def lerJogos():
    arq = open("database/games.json", encoding="utf-8")
    jogosJson = load(arq)

    jogos = []

    for j in jogosJson:
        jogos.append(Jogo(j, np.array(jogosJson[j]['categorias']).reshape(1, -1), jogosJson[j]['url']))

    return jogos

def salvar(similaridades):
    simJson = {}
    for sim in similaridades:
        simJson[sim.jogo.nome] = {
            'outros_jogos': sim.outros_jogos
        }
    arq = open('database/similaridades.json', 'w', encoding='utf-8')
    dump(simJson, arq, ensure_ascii=False)

"""
    Calcula a similaridade entre um jogo e outro usando o algoritmo "Cosine Similarity"
"""
def calcula_similaridade(conteudo_jogo, conteudo_outro_jogo):
    return cosine_similarity(conteudo_jogo, conteudo_outro_jogo)

"""
    Retorna uma lista com similaridade entre jogos: Todos X Todos
"""
def atualizar_scores(jogos):
    similaridades = []

    for jogo in jogos:
        conteudo_jogo = VectorSpaceModel.frequencias(jogo)
        similaridade  = Similaridade(jogo)
        print(jogo)
        for outro_jogo in jogos:
            if(not jogo is outro_jogo):
                conteudo_outro_jogo = VectorSpaceModel.frequencias(outro_jogo)
                score = calcula_similaridade(conteudo_jogo, conteudo_outro_jogo)
                similaridade.similar(outro_jogo, score)
                similaridades.append(similaridade)

    return similaridades

def main():
    jogos = lerJogos()
    similaridades = atualizar_scores(jogos)
    salvar(similaridades)

if __name__ == '__main__':
    main()
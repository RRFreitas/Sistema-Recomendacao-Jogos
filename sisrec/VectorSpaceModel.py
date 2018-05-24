from json import load
import numpy as np

def frequencias(jogo):
    arq = open("database/categorias.json", encoding="utf-8")
    categorias = load(arq)

    frequencia = []

    for categoria in categorias:
        if(categoria in jogo.categorias):
            frequencia.append(1)
        else:
            frequencia.append(0)

    frequencia = np.array(frequencia).reshape(1, -1)

    return frequencia
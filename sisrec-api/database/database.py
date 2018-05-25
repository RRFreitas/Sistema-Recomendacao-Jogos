# -*- coding: utf-8 -*-
from json import load

categorias = []
games = {}
similaridades = {}

def lerArquivos():
    with open("database/categorias.json", encoding="utf-8") as file:
        print("Reading categorias.json...")
        global categorias
        categorias = load(file)
    with open("database/games.json", encoding="utf-8") as file:
        print("Reading games.json...")
        global games
        games = load(file)
    with open("database/similaridades.json", encoding="utf-8") as file:
        print("Reading similaridades.json...")
        global similaridades
        similaridades = load(file)
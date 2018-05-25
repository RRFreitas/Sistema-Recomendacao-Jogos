import requests
from bs4 import BeautifulSoup
from models.Jogo import Jogo
from json import dump

mainUrl = "http://www.clickjogos.com.br/"

def getGamesUrl():
    page = requests.get("http://www.clickjogos.com.br/top/6meses/")
    soup = BeautifulSoup(page.content, 'html.parser')
    divGame = soup.findAll("div", {'class': 'game'})
    gamesA = [div.findAll("a", {'class': 'image'}, href=True) for div in divGame]
    urls = [a[0].get('href') for a in gamesA]

    return urls

def jogoConteudo(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    try:
        cabecalho = soup.find("div", {'class': 'h1_block'})
        nome = cabecalho.find('a').get_text()
        print(nome)
    except:
        return None

    nav = soup.find("ul", {'class': 'related_categories'})
    categorias = [c.get_text() for c in nav.select("span")]

    jogo = Jogo(nome, categorias, url)
    return jogo

def getGames():
    urls = getGamesUrl()
    games = []

    for url in urls:
        game = jogoConteudo(mainUrl + url)
        if(not game is None):
            games.append(game)

    return games

def salvarDados(games):
    jsonData = {}
    categorias = []

    for game in games:
        jsonData[game.nome] = {
            'categorias': game.categorias,
            'url': game.url
        }

        for c in game.categorias:
            if(not c in categorias):
                categorias.append(c)

    arq1 = open("database/games.json", "w", encoding="utf-8")
    arq2 = open("database/categorias.json", "w", encoding="utf-8")
    dump(jsonData, arq1, ensure_ascii=False)
    dump(categorias, arq2, ensure_ascii=False)

def main():
    games = getGames()
    salvarDados(games)

if __name__ == '__main__':
    main()
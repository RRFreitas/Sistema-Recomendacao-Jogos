class Jogo:
    def __init__(self, nome, categorias, url):
        self.nome = nome
        self.categorias = categorias
        self.url = url

    def __repr__(self):
        return "Jogo[nome = %s, categorias = %s, url = %s]" % (self.nome, self.categorias, self.url)
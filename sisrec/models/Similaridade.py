class Similaridade:
    def __init__(self, jogo):
        self.jogo = jogo
        self.outros_jogos = {}

    def similar(self, outro_jogo, score):
        self.outros_jogos[outro_jogo.nome] = score[0][0]

    def __repr__(self):
        return "Similaridade[jogo = %s, outro_jogos = %s]" % (self.jogo.nome, self.outros_jogos)
from Domain.Leilao import Leilao

class Avaliador:
    def __init__(self):
        self.menor_valor = None
        self.maior_valor = None

    def avaliar(self, leilao: Leilao):
        primeira_avaliacao = False
        for lance in leilao.lances:
            if (primeira_avaliacao == False):
                self.menor_valor = lance
                self.maior_valor = lance
                primeira_avaliacao = True
            else:
                if(lance.valor <= self.menor_valor.valor):
                    self.menor_valor = lance
                if(lance.valor >= self.maior_valor.valor):
                    self.maior_valor = lance


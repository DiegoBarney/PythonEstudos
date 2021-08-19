import unittest
from Domain.Usuario import Usuario
from Domain.Lance import Lance
from Domain.Leilao import Leilao
from Domain.Avaliador import Avaliador

class Test_Avaliador(unittest.TestCase):

    def test_Avaliar(self):
        usuario = Usuario('Diego')
        lance1 = Lance(usuario, 100)
        lance2 = Lance(usuario, 200)
        lance3 = Lance(usuario, 50)

        leilao = Leilao('CIVIC 2011')

        leilao.propoe(lance2)
        leilao.propoe(lance1)
        leilao.propoe(lance3)

        avaliador = Avaliador()
        avaliador.avaliar(leilao)
        self.assertTrue(avaliador.menor_valor.valor == 50)
        self.assertTrue(avaliador.maior_valor.valor == 200)



if __name__ == '__main__':
    unittest.main()

from Domain.Usuario import Usuario
from Domain.Lance import Lance
from Domain.Leilao import Leilao
from Domain.Avaliador import Avaliador


usuari = Usuario('Diego')
lance1 = Lance(usuari, 100)
lance2 = Lance(usuari, 200)

leila = Leilao('CIVIC 2011')

leila.lances = lance2
leila.lances = lance1


avaliador = Avaliador()
avaliador.avaliar(leila)

print(avaliador.menor_valor.valor)
print(avaliador.maior_valor.valor)
print(leila.lances[1])




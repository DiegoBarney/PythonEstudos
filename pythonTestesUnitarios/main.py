from Domain.Usuario import Usuario
from Domain.Lance import Lance
from Domain.Leilao import Leilao


usuari = Usuario('Diego')
lance1 = Lance(usuari, 100)
lance2 = Lance(usuari, 200)

leila = Leilao('CIVIC 2011')

leila.lances = lance1
leila.lances = lance2

print(leila.lances[0])




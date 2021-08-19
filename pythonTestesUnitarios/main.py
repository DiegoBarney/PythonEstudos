from Domain.Usuario import Usuario
from Domain.Lance import Lance
from Domain.Leilao import Leilao
from Domain.Avaliador import Avaliador


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

print("Menor lance: " + str(avaliador.menor_valor.valor))
print("Maior lance: " + str(avaliador.maior_valor.valor))
print(leilao.lances[1])




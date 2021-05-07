import Serie
import Filme
import Programa

vingadores = Filme.Filme("vingadores guerra infinita", 2018, 160)
vingadores.dar_like()

breakingbad = Serie.Serie("breaking Bad", 2008, 8)
breakingbad.dar_like()
breakingbad.dar_like()


lista_series_filmes = [breakingbad, vingadores]

for programa in lista_series_filmes:
    if type(programa) is Serie.Serie:
        print("Nome: {0}, Ano = {1}, temporadas = {2}".format(programa.nome, programa.ano, programa.temporadas))
    else:
        print("Nome: {0}, Ano = {1}, temporadas = {2}".format(programa.nome, programa.ano, programa.duracao))
        

print("Nome: {0}, likes: {1}".format(vingadores.nome, vingadores.likes))


import Serie
import Filme
import Playlist
import Programa
from collections.abc import Sized


vingadores = Filme.Filme("vingadores guerra infinita", 2018, 160)
vingadores.dar_like()

breakingbad = Serie.Serie("breaking Bad", 2008, 8)
breakingbad.dar_like()
breakingbad.dar_like()


got = Serie.Serie("game of thrones", 2011, 9)

list_programas = [got, vingadores, breakingbad]

play_list_fim_de_semana = Playlist.Playlist("Fim de Semana", list_programas)



#lista_series_filmes = [breakingbad, vingadores]
print(play_list_fim_de_semana.nome)
print("tamanho = ",len(play_list_fim_de_semana))
for programa in play_list_fim_de_semana:
    print(programa)
  #  if type(programa) is Serie.Serie:
   #     print("Nome: {0}, Ano = {1}, temporadas = {2}".format(programa.nome, programa.ano, programa.temporadas))
    #else:
     #   print("Nome: {0}, Ano = {1}, temporadas = {2}".format(programa.nome, programa.ano, programa.duracao))
        

#print("Nome: {0}, likes: {1}".format(vingadores.nome, vingadores.likes))


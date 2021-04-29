import PythonAdivinha
import PythonForca
import random

#PythonAdivinha.JogoAdvinha()

arquivo = open("palavras.txt", "w")

arquivo.write("manga\n");
arquivo.write("pera\n");
arquivo.write("uva\n");
arquivo.write("jabuticaba\n");

arquivo.close()

arquivo = open("palavras.txt", "r")

palavras = arquivo.readlines()

palavrasNew = []

for palavra in palavras:
    palavrasNew.append(palavra.strip())

arquivo.close()

posicao = random.randrange(0, len(palavrasNew));

PythonForca.JogoForca(palavrasNew[posicao])
#soma = PythonAdivinha.somar(1,5)

#print("Soma = ", soma);


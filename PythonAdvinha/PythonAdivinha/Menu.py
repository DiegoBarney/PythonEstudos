import PythonAdivinha
import PythonForca

#PythonAdivinha.JogoAdvinha()

arquivo = open("palavras.txt", "w")

arquivo.write("manga\n");
arquivo.write("pera\n");
arquivo.write("uva\n");
arquivo.write("jabuticaba\n");

arquivo.close()

arquivo = open("palavras.txt", "r")

palavras = arquivo.readlines()

palavrasnew = []

for palavra in palavras:
    palavrasnew.append(palavra.strip())

arquivo.close()

PythonForca.JogoForca(palavrasnew)
#soma = PythonAdivinha.somar(1,5)

#print("Soma = ", soma);


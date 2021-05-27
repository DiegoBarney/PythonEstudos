
idades_do_ano = [18,20,33,21,60]


idades_maior_vinte = [(idade+1) for idade in idades_do_ano]

print(idades_maior_vinte)

idades_maior_vinte = [(idade) for idade in idades_do_ano if idade > 20]

print(idades_maior_vinte)
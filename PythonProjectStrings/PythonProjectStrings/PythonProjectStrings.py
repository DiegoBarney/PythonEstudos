from Extrator import ExtratorArgumentoURL
from Padrao import PadroesUtils

url = "google.com.br"
telefone = "meu telefone é 96485-5252, favor ligar no horario comercial, caso não atender ligar em 95545-2222"



PadroesUtils.encontra_telefones(telefone)
print(ExtratorArgumentoURL.string_eh_valida(url))
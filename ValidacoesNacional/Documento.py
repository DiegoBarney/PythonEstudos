
class Documento:
    def __init__(self, doc):
        if (len(str(doc)) == 11):
            print("is cpf")
        if (len(str(doc)) == 9):
            print("is rg")

    def valida_documento(self, documento):
        if( len( str(documento) ) == 11):
            print("is cpf")
        if (len(str(documento)) == 9):
            print("is rg")





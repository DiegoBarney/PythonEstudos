class Lance:
    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor

    def __str__(self):
        return "{}-{}".format(self.usuario, self.valor)
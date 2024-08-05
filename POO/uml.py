class Escritor:
    def __init__(self, nome):
        self.nome = nome
        self._ferramenta = None

    @property
    def ferramenta(self):
        return self._ferramenta

    @ferramenta.setter
    def ferramenta(self, valor):
        self._ferramenta = valor


class FerramentaDeEscrita:
    def __init__(self, nome):
        self.nome = nome

    def escrever(self):
        return f'{self.nome} está escrevendo'


escritor = Escritor('Allan')
caneta = FerramentaDeEscrita('Caneta bic')
Maquina = FerramentaDeEscrita(
    'Maquina de escrever da epoca que tua vó ainda era sexy')

print(caneta.escrever(), escritor.nome)

class Caneta:
    def __init__(self, cor):
        self._cor = cor
        self._cor_tampa = None

        # 'diz' para os devs que forem mexer no meu codigo, para não usar esse atributo

    @property
    def cor(self):
        return self._cor

    @cor.setter
    def cor(self, valor):
        self._cor = valor

    @property
    def cor_tampa(self):
        return self._cor_tampa

    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor


caneta = Caneta('Azul')

print(caneta.cor)
caneta.cor = 'Amarelo'
print(caneta.cor)
caneta.cor = 'rosa'
print(caneta.cor)

print(caneta.cor_tampa)  # -> None
caneta.cor_tampa = 'Azul'
print(caneta.cor_tampa)  # -> Azul

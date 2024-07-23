class Pessoa:
    # self referencía ao objeto em que a classe foi colocada | __init__ é uma das primeiras coisas a se inicializar num objeto.
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


p1 = Pessoa('Allan', 'Giovanni')


print(p1.nome, p1.sobrenome)

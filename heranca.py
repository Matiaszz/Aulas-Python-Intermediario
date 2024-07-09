class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_classe(self):  # MRO
        print('Classe PESSOA')


class Cliente(Pessoa):  # vai HERDAR de Pessoa (extends)
    def falar_classe(self):  # MRO
        print('Classe CLIENTE')


class Aluno(Pessoa):
    ...


c1 = Cliente('Allan', 'Giovanni')
c1.falar_classe()

c2 = Aluno('Matheus', 'José')
c2.falar_classe()

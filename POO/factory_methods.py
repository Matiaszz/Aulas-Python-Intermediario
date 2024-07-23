class Pessoa:
    ano = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod  # exemplo
    def normal(cls):
        print(f'Executei.')

    @classmethod
    def pessoa_50(cls, nome):  # -> cls = classe(Pessoa)
        return cls(nome, 50)


p = Pessoa('Allan', 17)

p50 = Pessoa.pessoa_50('Matheus')
p51 = Pessoa.pessoa_50('José')

print(p50.nome, p50.idade)
print(p51.nome, p51.idade)

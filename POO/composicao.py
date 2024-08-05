class Cliente:
    def __init__(self):
        self.endereco = []

    def inserir_endereco(self, rua, num):
        self.endereco.append(Endereco(rua, num))

    def listar_endereco(self):
        for end in self.endereco:
            print(end.rua, '-', end.num)


class Endereco:
    def __init__(self, rua, num):
        self.rua = rua
        self.num = num


client = Cliente()
client.inserir_endereco('Rua', 123)
client.inserir_endereco('Rua b', 456)
print(client.listar_endereco())

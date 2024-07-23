class Pessoa:
    ano = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_nascimento(self):
        # É melhor colocar o nome da classe.atributo em casos que eu queira um atributo da classe em si, por exemplo, se eu quiser um valor diferente dentro de um certo atributo, eu posso mexer internamente nele sem me preocupar com o da classe.
        return Pessoa.ano - self.idade

    def executable(self):
        print(f'{self.nome} nasceu em {self.get_nascimento()} ')


people = Pessoa('Allan', 17)  # a conta pode dar errado.

people.executable()

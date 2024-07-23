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


p1 = Pessoa('Allan', 17)  # a conta pode dar errado.


p1.nome = 'mudei'
p1.executable()

# Imprime um dicionario onde os atributos estão salvos | vars() faz a mesma coisa
print(p1.__dict__)


# Posso alterar e apagar valores da classe também dessa forma (não é muito comum) -> 'valor'
# p1.__dict__['chave'] = 'valor'
# print(p1.chave)

from dataclasses import dataclass


@dataclass
class Pessoa:
    nome: str
    sobrenome: str

    @property
    def nome_completo(self) -> str:
        return f'{self.nome} {self.sobrenome}'

    @nome_completo.setter
    def nome_completo(self, valor: str):
        nome, sobrenome = valor.split()
        self.nome = nome
        self.sobrenome = sobrenome


if __name__ == '__main__':
    p1 = Pessoa('Allan', 'Giovanni')
    p1.nome_completo = 'Matheus Jose'
    print(p1.nome_completo)

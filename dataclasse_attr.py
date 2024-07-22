from dataclasses import dataclass, asdict, astuple


@dataclass
class Pessoa:
    nome: str
    sobrenome: str


if __name__ == '__main__':
    p1 = Pessoa('Allan', 'Giovanni')
    print(asdict(p1).keys())  # --> Chaves
    print(asdict(p1).values())  # --> valores
    print(asdict(p1).items())  # --> Transforma a clase em dicionario
    print(astuple(p1)[1])  # --> Transforma a classe em tupla

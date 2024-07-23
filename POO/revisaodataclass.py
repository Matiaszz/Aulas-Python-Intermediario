from dataclasses import dataclass


@dataclass
class Pessoa:
    nome: str = 'Missing'
    idade: int = 0


@dataclass
class Compras(Pessoa):

    def lista_comprar(self, value: str):
        compras = []
        for i in value.split():
            compras.append(i)
        print(f'Lista atual: {compras}')


if __name__ == '__main__':
    p1 = Compras(nome='Allan', idade=17)
    print(1)
    p1.lista_comprar('i4 i5 i6')

    p2 = Compras(nome='Matheus', idade=38)
    print(2)
    p2.lista_comprar('i1 i2 i3')

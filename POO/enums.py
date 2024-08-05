# Enum -> Enumerações
# Enumerações na programação, são usadas em ocasiões onde temos
# um determinado número de coisas para escolher.
# Enums têm membros e seus valores são constantes.
# Enums em python:
#   - são um conjunto de nomes simbólicos (membros) ligados a valores únicos
#   - podem ser iterados para retornar seus membros canônicos na ordem de
#       definição
# enum.Enum é a superclasse para suas enumerações. Mas também pode ser usada
#   diretamente (mesmo assim, Enums não são classes normais em Python).
# Você poderá usar seu Enum com type annotations, com isinstance e
# outras coisas relacionadas com tipo.
# Para obter os dados:
# membro = Classe(valor), Classe['chave']
# chave = Classe.chave.name
# valor = Classe.chave.value
import enum

# Direcoes = enum.Enum('Direcoes', ['CIMA', 'BAIXO', 'ESQUERDA', 'DIREITA']) forma 1


class Direcoes(enum.Enum):
    ESQUERDA = 1
    DIREITA = 2
    CIMA = 3
    BAIXO = 4


def mover(direcao: Direcoes):

    if not isinstance(direcao, Direcoes):
        # Isso nunca vai ser executado (Python 3.11.8)
        raise ValueError('Direção não encontrada.')
    print(f'Movendo para { direcao.name}, ({direcao.value})')


mover(Direcoes.ESQUERDA)
mover(Direcoes.DIREITA)
mover(Direcoes.BAIXO)

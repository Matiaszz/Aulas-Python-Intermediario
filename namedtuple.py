# from collections import namedtuple

# carta = namedtuple('Carta',
#                    ['valor', 'naipe'],  # chave e valor, tipo dicionario
#                    # valor padrão para valor e naipe
#                    defaults=['PADRÃOV', 'PADRÃON']
#                    )
# as_espadas = carta('ás', 'Espadas')
# print(as_espadas.valor, as_espadas.naipe)

# for i in as_espadas:
#     print(i)

# Preferencia do professor abaixo
from typing import NamedTuple


class Carta(NamedTuple):
    valor: str = 'valor'
    naipe: str = 'naipe'


asespadas = Carta()
print(asespadas)

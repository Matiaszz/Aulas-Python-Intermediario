"""
Aprendendo a documentar funções

Uma breve descrição do codigo 
"""

var1 = 1


def soma(x: int | float, y: int | float) -> int | float:  # Tipo 1 de documentar
    """
    função para somar

    :param x: Numero 1
    :type x: int or float
                            # <-- Tipo 2 de documentar
    :param y: Numero 2  
    :type y: int or float

    :return: Soma de x e y
    :rtype: int or float


    """

    return x + y


def multiplica(x: int | float, y: int | float, z: int | float | None = None) -> int | float:
    if z is None:
        return x * y
    return x * y * z


var2 = 2

var3 = 3

print(multiplica(var2, var3))

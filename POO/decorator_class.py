
class Multiplicar:
    def __init__(self, func):
        self.func = func  # <-- Recebe a função

    def __call__(self, *args, **kwargs):
        results = self.func(*args)
        multiplicador = 10
        return results * multiplicador


@Multiplicar
def soma(x, y):
    return x + y


som = soma(3, 4)
print(som)

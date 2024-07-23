def add_repr(cls):
    def my_repr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name} | {class_dict}'
        return class_repr
    cls.__repr__ = my_repr
    return cls


def my_planet(method):
    def intern(self,  *args, **kwargs):
        results = method(self, *args, **kwargs)

        if 'terra' in results:
            return 'Está dentro de casa'
        return results

    return intern


def my_team(method):
    def intern(self, *args, **kwargs):
        results = method(self, *args, **kwargs)
        if results:
            return f'Seu time é: desconhecido'
    return intern


@add_repr
class Time:
    def __init__(self, nome):
        self.nome = nome

    @my_team
    def falar(self):
        return f'Seu time é: {self.nome}'


@add_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome

    @my_planet
    def falar(self):
        return f'Seu planeta é: {self.nome}'


corinthians = Time('Corinthians')
criciuma = Time('Criciume')

terra = Planeta('terra')
marte = Planeta('Marte')

print(corinthians)
print(criciuma)
print(terra)
print(marte)

print(terra.falar())
print(marte.falar())
print(criciuma.falar())

def add_repr(cls):
    def my_repr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name} | {class_dict}'
        return class_repr
    cls.__repr__ = my_repr
    return cls


@add_repr
class Time:
    def __init__(self, nome):
        self.nome = nome


@add_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome


corinthians = Time('Corinthians')
criciuma = Time('Criciume')

terra = Planeta('Terra')
marte = Planeta('Marte')

print(corinthians)
print(criciuma)
print(terra)
print(marte)

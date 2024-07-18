def reper(cls):
    def my_repr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name} | {class_dict}'
        print('meu repr')
        return class_repr
    cls.__repr__ = my_repr
    return cls


class Meta(type):
    def __new__(mcs, name, base, dct):
        print('Metaclass new')
        cls = super().__new__(mcs, name, base, dct)
        return cls

    def __call__(cls, *args, **kwargs):
        inst = super().__call__(*args, **kwargs)
        if 'nome' not in inst.__dict__:
            raise NotImplementedError('Crie o attr nome')
        return inst


@reper
class Pessoa(metaclass=Meta):
    def __new__(cls, *args, **kwargs):
        print('Meu new')
        inst = super().__new__(cls)
        return inst

    def __init__(self, nome):
        print('Meu init')
        self.nome = nome


allan = Pessoa('Allan')
print(allan)

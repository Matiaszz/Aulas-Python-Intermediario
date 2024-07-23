from abc import ABC, abstractmethod


class AbsFoo(ABC):
    def __init__(self, name):
        self._name = None
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    @abstractmethod
    def name(self, valor): ...


class Foo(AbsFoo):
    def __init__(self, name):
        super().__init__(name)

    @AbsFoo.name.setter
    def name(self, valor):
        self._name = valor


foo = Foo('Vl')
print(foo.name)

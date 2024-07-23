"""
Aprendendo a documentar Classes

é basicamente a mesma coisa da documentação de função, só que com classes

"""


class Foo:
    def soma(self, x: int | float, y: int | float) -> int | float:
        return x + y

    def multiplica(self, x: int | float, y: int | float, z: int | float | None = None) -> int | float:
        if z is None:
            return x * y
        return x * y * z

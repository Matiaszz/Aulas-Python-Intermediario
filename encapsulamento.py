class Foo:
    def __init__(self):
        self.public = 'Isso é publico'  # qualquer um pode acessar
        # (não deve ser usado fora da classe ou subclasse)
        self._protected = 'Isso é protegido '
        # (Só pode ser usado dentro da sua propria classe)
        self.__private = 'Isso é privado'

    def metodo_public(self):
        print(self.__metodo_private())
        print(self.__private)
        return

    def _metodo_protected(self):
        return 'Metodo protegido'

    def __metodo_private(self):
        return 'Metodo Privado'


f = Foo()
print(f.metodo_public())

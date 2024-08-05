# class MeuStr(str):
#     def upper(self):
#         print('Chamou upper')
#         return_str = super().upper()
#         print('Depois do super')
#         return return_str


# a = MeuStr('Allan')
# print(a.upper())


class A:

    atr_a = 'VALOR A'

    def __init__(self, atr):
        self.atr = atr

    def metodo(self):
        print('A')


class B(A):
    atr_b = 'VALOR B'

    def __init__(self, atr, outra):

        super().__init__(atr)
        self.outra = outra

    def metodo(self):
        print('B')


class C(B):
    atr_c = 'VALOR C'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # print('Init ta tudo certo')

    def metodo(self):
        # super().metodo()
        # super(B, self).metodo()  # -> A
        #     (A partir de (B) o método: .metodo(), então o super vai procurar na classe (A))
        print('C')


c = C('Atributo', 'qlqcoisa')

# c.metodo()  # -> B, A, C


# print(c.atr_a, c.atr_b, c.atr_c)

print(c.atr, c.outra)

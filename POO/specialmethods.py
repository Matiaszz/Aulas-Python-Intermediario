# Teoria: python Special Methods, Magic Methods ou Dunder Methods
# Dunder = Double Underscore = __dunder__
# Antigo e útil: https://rszalski.github.io/magicmethods/
# https://docs.python.org/3/reference/datamodel.html#specialnames
# __lt__(self,other) - self < other
# __le__(self,other) - self <= other
# __gt__(self,other) - self > other
# __ge__(self,other) - self >= other
# __eq__(self,other) - self == other
# __ne__(self,other) - self != other
# __add__(self,other) - self + other
# __sub__(self,other) - self - other
# __mul__(self,other) - self * other
# __truediv__(self,other) - self / other
# __neg__(self) - -self
# __str__(self) - str
# __repr__(self) - str
# !r - vê a representação de um objeto e deve ser colocado logo após o parametro do método

class Ponto:
    def __init__(self, x, y, z='STRING'):
        self.x = x
        self.y = y
        self.z = z

    # def __str__(self):  # Retornar a string de um objeto
    #     return str(__class__.__name__)

    def __repr__(self):  # Informar outros devs como o objeto é montado
        return f'{__class__.__name__}, x = {self.x!r} | y = {self.y!r} | z = {self.z!r}'

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Ponto(new_x, new_y)

    def __gt__(self, other):
        result_self = self.x + self.y
        result_other = other.x + other.y
        return result_self > result_other


p1 = Ponto(1, 2)
p2 = Ponto(34, 87)

# print(p1, '\n', p2)
p3 = p1 + p2
print(p3)  # 121, # 3
print(p1 > p2)  # False

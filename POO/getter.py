########## Primeira maneira de proteger um atributo##########
# class Caneta:
#     def __init__(self, cor):
#         self.cor_caneta = cor

#     def get_cor(self):
#         return self.cor_caneta


# can = Caneta('Azul')

# print(can.get_cor())


########### Segunda maneira de proteger uma atributo################

class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    @property
    def cor(self):
        return self.cor_tinta


caneta = Caneta('Azul')

print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)

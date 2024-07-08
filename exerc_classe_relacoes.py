class Carro:
    def __init__(self, nome, motor, fabricante):
        self.nome = nome
        self.motor = Motor(motor)
        self.fabricante = Fabricante(fabricante)

    def exibir(self):
        print(f'info \n Nome: {self.nome} \n Motor: {self.motor} \n Marca: {self.fabricante} \n <-------------------> ')

class Motor:
    def __init__(self, motor):
        self.motor = motor
    
    def __str__(self):
        return str(self.motor)
    

class Fabricante:
    def __init__(self, fabricante):
        self.fabricante = fabricante
        
    def __str__(self):
        return str(self.fabricante)


c1 = Carro('Uno', 'Mile', 'Fiat')
c1.exibir()

c2 = Carro('F1', 'V6', 'McLaren')
c2.exibir()
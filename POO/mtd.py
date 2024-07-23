class Car():
    def __init__(self, name):
        self.name = name

    def accelerate(self):
        print(f'{self.name} está acelerando')


gol = Car('Gol')

gol.accelerate()

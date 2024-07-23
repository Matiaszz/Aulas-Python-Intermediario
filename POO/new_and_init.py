class A:
    def __new__(cls, *args, **kwargs):
        print('123')
        print('Até aqui, eu posso fazer algo antes de criar a instancia')
        instance = super().__new__(cls)
        return instance
        # depois o init é executado

    def __init__(self, x):
        self.x = x
        print(self)

    def __repr__(self):
        return f'{__class__.__name__}'


a = A('Valor do x')
print(a.x)

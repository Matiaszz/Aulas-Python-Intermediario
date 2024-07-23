from abc import ABC, abstractmethod


class Pessoa(ABC):
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self._conta = None

    @property
    def conta(self):
        return self._conta

    @conta.setter
    def conta(self, conta):
        self._conta = conta


class Conta(ABC):
    def __init__(self, agencia, numero_conta, saldo=0):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.saldo = saldo

    @abstractmethod
    def depositar(self, valor):
        pass

    @abstractmethod
    def sacar(self, valor):
        pass


class ContaCorrente(Conta):
    def __init__(self, agencia, numero_conta, saldo=0, limite_extra=0):
        super().__init__(agencia, numero_conta, saldo)
        self.limite_extra = limite_extra

    def depositar(self, valor):
        self.saldo += valor
        print(f'Depositado: {valor}. Saldo atual: {self.saldo}')

    def sacar(self, valor):
        if self.saldo + self.limite_extra >= valor:
            self.saldo -= valor
            print(f'Sacado: {valor}. Saldo atual: {self.saldo}')
        else:
            print('Saldo insuficiente')


class ContaPoupanca(Conta):
    def depositar(self, valor):
        self.saldo += valor
        print(f'Depositado: {valor}. Saldo atual: {self.saldo}')

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f'Sacado: {valor}. Saldo atual: {self.saldo}')
        else:
            print('Saldo insuficiente')


class Banco:
    def __init__(self):
        self.clientes = []
        self.contas = []

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def autenticar(self, cliente, conta):
        return cliente in self.clientes and conta in self.contas and conta.agencia == cliente.conta.agencia

    def sacar(self, cliente, conta, valor):
        if self.autenticar(cliente, conta):
            conta.sacar(valor)
        else:
            print("Autenticação falhou")

    def depositar(self, cliente, conta, valor):
        if self.autenticar(cliente, conta):
            conta.depositar(valor)
        else:
            print("Autenticação falhou")


# Exemplo de uso:
banco = Banco()

# Criando cliente e contas
cliente1 = Cliente('Allan', 17)
conta_corrente = ContaCorrente('001', '1234', saldo=1000, limite_extra=500)
conta_poupanca = ContaPoupanca('001', '5678', saldo=1500)

# Associando conta ao cliente
cliente1.conta = conta_corrente

# Adicionando cliente e conta ao banco
banco.adicionar_cliente(cliente1)
banco.adicionar_conta(conta_corrente)
banco.adicionar_conta(conta_poupanca)

# Realizando operações
banco.depositar(cliente1, conta_corrente, 200)
banco.sacar(cliente1, conta_corrente, 500)
banco.sacar(cliente1, conta_corrente, 2000)
banco.depositar(cliente1, conta_poupanca, 100)
banco.sacar(cliente1, conta_poupanca, 300)

from abc import ABC, abstractmethod


class Conta:

    def __init__(self, agencia: int, conta: int, saldo: float = 0) -> None:
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abstractmethod
    def sacar(self) -> float:
        pass

    def depositar(self, valor: float) -> float:
        self.saldo += valor
        self.detalhes(f'Deposito... {valor} ')
        return self.saldo

    def detalhes(self, msg='') -> None:
        print(f'O seu saldo é: {self.saldo:.2f} | {msg}')

    def __repr__(self) -> str:
        dic = f'{self.agencia!r}, {self.conta!r}, {self.saldo!r}'

        return f'{__class__.__name__} | {dic} '


class ContaPoupanca(Conta):
    def sacar(self, valor: float) -> float:
        valor_saque = self.saldo - valor

        if valor_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'Sacando... {valor}')
            return self.saldo

        print('Não foi possivel sacar o valor desejado.')
        self.detalhes('Saque negado.')
        return self.saldo


class ContaCorrente(Conta):
    def __init__(self, agencia: int, conta: int, saldo: int = 0, extra: float = 0):
        super().__init__(agencia, conta, saldo)
        self.extra = extra

    def sacar(self, valor: int) -> float:
        valor_saque = self.saldo - valor
        limite_max = -self.extra

        if valor_saque >= limite_max:
            self.saldo -= valor
            self.detalhes(f'Sacando... {valor}')
            return self.saldo

        print('Não foi possivel sacar o valor desejado.')
        self.detalhes(f'Seu limite é: {-self.extra:.2f}')
        self.detalhes(f'Saque negado.({valor})')
        return self.saldo

    def __repr__(self) -> str:
        dic = f'{self.agencia!r}, {self.conta!r}, {self.saldo!r} {self.extra!r}'
        return f'{__class__.__name__} | {dic} '


if __name__ == '__main__':
    cp1 = ContaPoupanca(111, 222)
    cp1.sacar(1)
    cp1.depositar(1)
    cp1.sacar(1)
    cp1.sacar(1)
    print('##')

    cc1 = ContaCorrente(111, 222, 0, 100)

    cc1.sacar(1)
    cc1.depositar(1)
    cc1.sacar(1)
    cc1.sacar(1)
    cc1.sacar(98)
    cc1.sacar(1)
    print('##')

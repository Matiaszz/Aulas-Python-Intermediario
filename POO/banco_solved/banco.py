import contas
import pessoa


class Banco:
    def __init__(self,
                 agencias: list[int] | None = None,
                 clientes: list[pessoa.Pessoa] | None = None,
                 contas: list[contas.Conta] | None = None):

        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []

    def _checa_agencia(self, conta):
        if conta.agencia in self.agencias:
            print('True')
            return True
        print('False')
        return False

    def _checa_cliente(self, cliente):
        if cliente in self.clientes:
            print('True')
            return True
        print('False')
        return False

    def _checa_conta(self, conta):
        if conta in self.contas:
            print('True')
            return True
        print('False')
        return False

    def valida_conta(self, cliente, conta):
        if conta is cliente.conta:
            print('True')
            return True
        print('False')
        return False

    def autenticar(self, cliente: pessoa.Cliente, conta: contas.Conta):
        return self._checa_agencia(conta) and self._checa_cliente(cliente) and self._checa_conta(conta) and self.valida_conta(cliente, conta)

    def __repr__(self) -> str:
        dic = f'{self.agencias!r}, {self.clientes!r}, {self.contas!r}'
        return f' \n{__class__.__name__} | {dic} '


if __name__ == '__main__':

    c1 = pessoa.Cliente('Allan', 17)
    c1.conta = contas.ContaCorrente(123, 777, 0, 0)

    c2 = pessoa.Cliente('Matheus', 48)
    c2.conta = contas.ContaPoupanca(333, 444, 100)

    banco = Banco()
    banco.clientes.extend([c1, c2])
    banco.contas.extend([c1.conta, c2.conta])
    banco.agencias.extend([123, 222])

    print(banco.autenticar(c1, c1.conta))
    if banco.autenticar(c1, c1.conta):
        c1.conta.depositar(10)
        c1.conta.sacar(9)

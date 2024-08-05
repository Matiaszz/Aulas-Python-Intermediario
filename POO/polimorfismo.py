from abc import ABC, abstractmethod


class Notificacao(ABC):
    def __init__(self, msg) -> None:
        self.msg = msg

    @abstractmethod
    def enviar(self) -> bool:
        pass


class SmsNot(Notificacao):

    def enviar(self) -> bool:
        print(f'{self.msg}, SMS')
        return True


class EmailNot(Notificacao):
    def enviar(self):
        print(f'{self.msg}, Email')
        return False


def notificar(notificacao: Notificacao):
    not_send = notificacao.enviar()
    if not_send:
        print('Notificação enviada.')
    else:
        print('Não foi enviada')


email = EmailNot('Mensagem')
sms = SmsNot('Mensagem')
notificar(sms)
notificar(email)

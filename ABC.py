from abc import ABC, abstractmethod


class Log(ABC):  # <-- tem que herdar de abc para criar um método abstrato(abstract class method)
    @abstractmethod  # <-- gera um 'contrato' para dizer 'Você tem que instanciar esse método'
    def _log(self, msg): ...

    def logError(self, msg):
        return self._log(f'Error: {msg}')

    def logSucess(self, msg):
        return self._log(f'Sucess: {msg}')


class LogPrintMixin(Log):  # <-- O que vai aparecer no terminal
    def _log(self, msg):
        print(f'{msg}, {__class__.__name__}')

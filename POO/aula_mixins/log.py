# Abstração
from pathlib import Path
DIR_LOG = Path(__file__).parent / 'log.txt'


class Log:  # <-- Super Classe
    def _log(self, msg):  # <-- Fala para os outros devs não usarem esse método fora da familia
        raise NotImplementedError('Implemente um método')

    def logError(self, msg):
        return self._log(f'Error: {msg}')

    def logSucess(self, msg):
        return self._log(f'Sucess: {msg}')


class LogFileMixin(Log):  # <-- Método de salvamento de LOG
    def _log(self, msg):
        formated_msg = f'{msg}, [{__class__.__name__}]'
        try:
            with open(DIR_LOG, 'a', encoding='utf-8') as file:
                file.write(formated_msg)
                file.write('\n \n')
        except FileNotFoundError:
            with open(DIR_LOG, 'w', encoding='utf-8') as file:
                file.write(formated_msg)
                file.write('\n \n')


class LogPrintMixin(Log):  # <-- O que vai aparecer no terminal
    def _log(self, msg):

        print(f'{msg}, {__class__.__name__}')


def mainLog():  # <-- area de testes
    print('Salvando...')
    lf = LogFileMixin()
    lf.logSucess('Só sucesso pai')
    lf.logError('Exemplo de algum erro que deu')

    lp = LogPrintMixin()
    lp.logSucess('Só sucesso pai')
    lp.logError('Exemplo de algum erro que deu')
    return


if __name__ == '__main__':

    mainLog()

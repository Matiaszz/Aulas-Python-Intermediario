from log import LogFileMixin


class Eletronic:
    def __init__(self, nome):
        self._nome = nome
        self._on = False

    def turn_on(self):
        if not self._on:
            self._on = True

    def turn_off(self):
        if self._on:
            self._on = False


class SmartPhone(Eletronic, LogFileMixin):

    def turn_on(self):
        super().turn_on()

        if self._on:
            f_msg = f'{self._nome} está ligado!'
            return self.logSucess(f_msg)

    def turn_off(self):
        super().turn_off()

        if not self._on:
            f_msg = f'{self._nome} está desligado!'
            return self.logError(f_msg)

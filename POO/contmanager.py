class ContextManager:
    def __init__(self, adress, mode):
        self._adress = adress
        self._mode = mode
        self._fileOpen = None

    def __enter__(self):
        print('Abrindo')
        self._fileOpen = open(self._adress, self._mode, encoding='utf8')
        return self._fileOpen
        # o retorno do enter vai para a variavel do with

    def __exit__(self, class_exception, exception_, traceback_):
        print('Fechando')
        self._fileOpen.close()  # type: ignore
        exception_.add_note(
            f'Tem algum erro na forma que voce executou a classe')


inst = ContextManager('ContextManager.txt', 'w')
with inst as var:
    var.write('Mercúrio')

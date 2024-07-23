from contextlib import contextmanager


@contextmanager
def my_open(adress, mode):
    try:
        print('Abrindo arquivo')
        file = open(adress, mode, encoding='utf8')
        # vai tentar abrir o arquivo, executar o que o usuario  pede e de qualquer forma fechar o arquivo.
        yield file

    except Exception as e:
        print(f'Ocorreu um erro: {e}')

    finally:
        print('Fechando')
        file.close()


with my_open('teste.txt', 'w') as file:
    file.write('Linha 1 \n')
    file.write('Linha 2 \n')
    file.write('Linha 3 \n')

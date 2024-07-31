
import sys

args = sys.argv + ['Argumento 1 ', 'Argumento 2']  # sistema recebe argumentos
qtd_args = len(args)


if qtd_args <= 1:
    print('Não passou argumentos.')
else:
    try:
        print(f'Você passou os argumentos: {args[1:]}')
        print(f'Argumento 1: {args[1]}')
        print(f'Arguento 2: {args[2]}')
    except IndexError:
        print('erro')

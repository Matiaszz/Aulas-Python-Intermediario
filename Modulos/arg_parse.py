# win: python .\Modulos\arg_parse.py -b
from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument(
    '-b', '--basic',
    help='Mostra o valor de basic, se tiver valor padrão, mostra ele.',
    # type=str, #define o tipo do argumento recebido
    metavar='STRING',
    # default='Olá mundo!',
    required=True,
    action='append',  # recebe o argumento mais de uma vez
    # nargs='+', #recebe mais de um valor
)
args_parser = parser.parse_args()

if args_parser is None:
    print(f'Passe o valor de: {args_parser.basic}')
else:
    print(args_parser.basic)

import math
import os


def formata_tamanho(tamanho_em_bytes: int, base: int = 1000) -> str:
    """Formata um tamanho, de bytes para o tamanho apropriado"""

    # Original:
    # https://stackoverflow.com/questions/5194057/better-way-to-convert-file-sizes-in-python

    # Se o tamanho for menor ou igual a 0, retorne 0B.
    if tamanho_em_bytes <= 0:
        return "0B"

    # Tupla com os tamanhos
    #                      0    1     2     3     4     5
    abreviacao_tamanhos = "B", "KB", "MB", "GB", "TB", "PB"

    # Logaritmo -> https://brasilescola.uol.com.br/matematica/logaritmo.htm
    # math.log vai retornar o logaritmo do tamanho_em_bytes
    # com a base (1000 por padrão), isso deve bater
    # com o nosso índice na abreviação dos tamanhos
    indice_abreviacao_tamanhos = int(math.log(tamanho_em_bytes, base))

    # Por quanto nosso tamanho deve ser dividido para gerar o tamanho correto.
    potencia = base ** indice_abreviacao_tamanhos

    # Nosso tamanho final
    tamanho_final = tamanho_em_bytes / potencia
    # A abreviação que queremos
    abreviacao_tamanho = abreviacao_tamanhos[indice_abreviacao_tamanhos]
    return f'{tamanho_final:.2f} {abreviacao_tamanho}'


adress = 'C:\\Users\\User\\Pictures\\Screenshots\\'

counter = 0

for root, dirs, files in os.walk(adress):

    counter += 1

    print(' ',  counter, 'Pasta: ', root)

    for dir_ in dirs:
        print('\t', counter, 'Dir: ', *dirs)

    for file in files:
        complete_adress = os.path.join(root, file)
        size = os.path.getsize(complete_adress)

        print('\t', counter, 'File: ', file, formata_tamanho(size))

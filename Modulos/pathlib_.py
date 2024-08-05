from pathlib import Path

this_folder = Path()
this_file = Path(__file__)

# print(this_file)  # ESSE ARQUIVO

# print(this_folder.absolute())  # PASTA AULAS_PYTHON_POO

# print(this_file.parent)  # PASTA MODULOS

# PASTA AULAS PYTHON POO (posso usar quantos parents precisar)
# print(this_file.parent.parent)

# / - cria um novo arquivo ou pasta

# new_folder = this_file.parent / 'Folder_example'
# ==> c:\Users\User\Desktop\Aulas_Python_POO\Modulos\Folder_example


# print(new_folder / 'arquivo.txt')
# ==> c:\Users\User\Desktop\Aulas_Python_POO\Modulos\Folder_example\arquivo.txt

# print(Path.home())
# ==> C:\Users\User

file = Path.home() / 'Desktop' / 'arquivo.txt'

# Cria o arquivo na maquina mesmo
file.touch()


# escreve um texto no arquivo
# file.write_text('Escrevi outro texto (área)', encoding='utf8')

# print(file.read_text(encoding='utf8')) # lê o arquivo

with open(file, 'a+', encoding='utf8') as txt:
    txt.write('Escrevi um texto (Pó de sabão) \n')
    txt.write('Ozônio \n')

with open(file, 'r', encoding='utf8') as txt:
    print(txt.read())

file.unlink()
##############################################################################
# adress_folder = Path.home() / 'Desktop' / 'Pasta criada'
# adress_folder.mkdir(exist_ok=True)

# subfolder = adress_folder / 'Subpasta'
# subfolder.mkdir(exist_ok=True)

# other_file = subfolder / 'Outro arquivo.txt'
# other_file.touch()
# other_file.write_text('Olá mundo', encoding='utf8')

# para apagar uma pasta, tem que apagar todos os arquivos dentro dela primeiro

# other_file.unlink()  # apaga o arquivo dentro da subpasta
# subfolder.rmdir()  # apaga a subpasta
# adress_folder.rmdir()  # apaga o pai da subpasta

adress_folder = Path.home() / 'Desktop' / 'Pasta criada'
adress_folder.mkdir(exist_ok=True)
files = adress_folder / 'files'
files.mkdir(exist_ok=True)

for i in range(11):
    file = files / f'file_{i}.txt'

    if file.exists():
        file.unlink()
    else:
        file.touch()

    with open(file, 'a+') as txt:
        txt.write('Olá mundo \n')

        txt.write(f'Sou eu, o tiririca! {i} \n')


def rmtree(root: Path, remove_root=True):

    for file in root.glob('*'):

        if file.is_dir():
            print('DIR: ', file)
            rmtree(file, remove_root=False)
            file.rmdir()
        else:
            print(f'file: {file}')
            file.unlink()
    if remove_root:
        root.rmdir()


# rmtree(adress_folder)

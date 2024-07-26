import os
import shutil

HOME = os.path.expanduser('~')
IMAGES = os.path.join(HOME, 'Pictures', 'Screenshots')
ORIGINAL_FOLDER = os.path.join(IMAGES, 'EXEMPLO')
NEW_FOLDER = os.path.join(IMAGES, 'EXEMPLO2')
OTHER_FOLDER = os.path.join(IMAGES, 'PASTACRIADA')

os.makedirs(OTHER_FOLDER, exist_ok=True)  # cria outra pasta

for root, dirs, files in os.walk(IMAGES):
    # root: tudo que esta dentro de Screenshots
    for dir_ in dirs:
        # altera o root para que seja o diretorio
        caminnho_novo_diretorio = os.path.join(
            root.replace(IMAGES, OTHER_FOLDER), dir_
        )

        os.makedirs(caminnho_novo_diretorio, exist_ok=True)

    for file in files:
        caminho_arquivo = os.path.join(root, file)

        caminnho_novo_arquivo = os.path.join(
            # altera o root para que ele seja o destinatario
            root.replace(IMAGES, OTHER_FOLDER), file
        )

        # da onde quer copiar os arquivos, onde quer coloca-los
        shutil.copy(caminho_arquivo, caminnho_novo_arquivo)

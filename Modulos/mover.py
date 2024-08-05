import os
import shutil

HOME = os.path.expanduser('~')
IMAGES = os.path.join(HOME, 'Pictures', 'Screenshots')
NEW_FOLDER = os.path.join(IMAGES, 'EXEMPLO2')
OTHER_FOLDER = os.path.join(IMAGES, 'PASTACRIADA')


shutil.rmtree(OTHER_FOLDER, ignore_errors=True)
shutil.copytree(IMAGES, OTHER_FOLDER)
shutil.move(NEW_FOLDER, OTHER_FOLDER + '_EITA')

# Copiar itens de uma pasta para outra de forma mais facil

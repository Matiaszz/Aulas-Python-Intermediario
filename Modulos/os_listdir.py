import os
adress = 'C:\\Users\\User\\Pictures\\Screenshots\\'

for file in os.listdir(adress):
    new_adress = adress + file  # adiciona os arquivos no diretorio

    if not os.path.isdir(new_adress):
        # se for diretorio, continue para o outro for
        continue

    print(file, '\n', '-'*20)
    for img in os.listdir(new_adress):
        # exibe o caminho completo para cada imagem
        print(new_adress + '\\' + img)

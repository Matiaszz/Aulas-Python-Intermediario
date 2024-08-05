import os

adress = 'C:\\Users\\User\\Pictures\\Screenshots\\'

counter = 0
for root, dirs, files in os.walk(adress):

    counter += 1

    print(' ',  counter, 'Pasta: ', root)

    for dir_ in dirs:
        print('\t', counter, 'Dir: ', *dirs)

    for file in files:
        complete_adress = os.path.join(root, file)
        print('\t', counter, 'File: ', complete_adress)

        # NÃO EXECUTE, VAI APAGAR TUDO (não vai pra lixeira, exclui direto)
        # os.unlink(complete_adress)

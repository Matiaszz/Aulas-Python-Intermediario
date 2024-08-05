import os

caminho = os.path.join('Desktop', 'Aulas_Python_POO', 'os.py')

# recebe uma tupla com 2 valores contendo o diretorio e o arquivo separado
diretorio = os.path.split(caminho)

# desempacota a tupla nessas 2 variaveis
diretorio2, arquivo = os.path.split(caminho)

# recebe uma tupla com o diretorio e o nome do arquivo sem a extensão e a
# extensão separado
# pode usar a regra de cima nesse splitext tbm
nome_arquivo, extensao = os.path.splitext(caminho)
print(nome_arquivo, extensao)

# retorna true ou false (se o arquivo existe ou não)
print(os.path.exists
      ('C:\\Users\\User\\Desktop\\Aulas_Python_POO\\POO\\ABC.py')
      )

# retorna o caminho DESSE ARQUIVO (representado como '.')
print(os.path.abspath('.'))


# retorna o ultimo arquivo
print(os.path.basename(caminho))

# retorna o diretorio
print(os.path.dirname(caminho))

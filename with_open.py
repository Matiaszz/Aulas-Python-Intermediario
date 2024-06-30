caminho_arq = 'C:\\Users\\User\\Desktop\\AulasPython\\'
caminho_arq += 'aulas.txt'  # Cria um arquivo ou edita ele se já tiver

# abre e fecha automaticamente um arquivo depois do codigo ser executado
with open(caminho_arq, 'w+') as arquivo:
    arquivo.write('Ler\n')
    # escreve uma linha no arquivo
    arquivo.writelines(('Linha 1\n', 'Linha 2\n'))
    # escreve mais de uma linha no arquivo(valores tem que ser passados em tuplas)
    arquivo.seek(0, 0)
    print('#' * 15)
    print('READ')
    # move o cursor para o inicio da pagina, tornando o arquivo legivel
    print(arquivo.read().strip())
    # lê o arquivo inteiro
    # .strip(remove todos os espaços que tiver no meio ou no final do print se ele for str)
    arquivo.seek(0, 0)
    # move o cursor para o inicio da pagina de novo(pois nesse momento ele está no final,  porque ele leu li todas as linhas)
    print('#' * 15)

    print('READLINE')
    print(arquivo.readline().strip())
    # lê uma linha por vez

    print(arquivo.readline().strip())
    print(arquivo.readline().strip())

    print('#' * 15)

    print('READLINES')
    arquivo.seek(0, 0)
    for linha in arquivo.readlines():
        print(linha, end='')

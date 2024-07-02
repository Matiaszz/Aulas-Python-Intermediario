import os

tasks = []
pops = []
commands = 'listar', 'desfazer', 'refazer', 'limpar', 'sair'
FILE_SAVE = 'C:\\Users\\User\\Desktop\\AulasPython\\'
FILE_SAVE += 'Lista_de_tarefas.txt'


def undo():
    try:
        item = tasks.pop()
        pops.append(item)
    except IndexError:
        print()
        print('Nada para desfazer.')
        print()
        print()


def remake():
    if pops == []:
        print('Nada a refazer.')
    else:
        last_index = pops.pop()
        tasks.append(last_index)


while True:
    print('Comandos')
    print('LISTAR', 'DESFAZER', 'REFAZER', 'SAIR')
    value = input(
        'Digite um comando ou uma tarefa para adicionar: ').lower().strip()

    if value not in commands:
        os.system('cls')
        tasks.append(value)

    elif value == 'desfazer':
        os.system('cls')
        undo()

    elif value == 'refazer':
        os.system('cls')
        remake()

    elif value == 'listar':
        os.system('cls')
        print()
        print('-' * 5, 'ITENS NA LISTA', '-' * 5)
        with open(FILE_SAVE, 'w+', encoding='utf-8') as file:
            print('Itens que só podem ser alterados manualmente -🔹:')
            print(file.read())

        for item_task in tasks:
            print(item_task)
        print('-' * 30)
        print()

    elif value == 'sair':
        print('-- Lista de Tarefas Salva - Programa Encerrado --')
        with open('C:\\Users\\user\\desktop\\AulasPython\\lista_de_tarefas.txt', 'a', encoding='utf-8') as file:
            file.write(
                '\n'.join(['🔹' + task + '\n' for task in tasks]) + '----------SAVE----------' + '\n')
        break

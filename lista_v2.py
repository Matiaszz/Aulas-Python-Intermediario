import sys
import json


FILE_SAVE = 'lista_v2.json'


def exit_func():
    print('-- Lista de Tarefas Salva - Programa Encerrado --')
    sys.exit()


def items_list(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return

    print('Tarefas:')
    for tarefa in tarefas:
        print(tarefa)
    print()


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
        return
    last_index = pops.pop()
    tasks.append(last_index)


def read_tasks(tasks, adress):
    try:

        with open(adress, 'r', encoding='utf8') as file:
            data = json.load(file)
    except FileNotFoundError:
        save(tasks, adress)
    return data


def save(task, adress):
    data = task
    with open(adress, 'w', encoding='utf8') as file:
        data = json.dump(task, file, indent=2)
    return data


tasks = read_tasks([], FILE_SAVE)
pops = []
while True:
    print('Comandos')
    print('LISTAR', 'DESFAZER', 'REFAZER', 'SAIR')
    value = input(
        'Digite um comando ou uma tarefa para adicionar: ').lower().strip()
    commands_list = {
        'listar': lambda: items_list(tasks),
        'desfazer': lambda: undo(),
        'refazer': lambda: remake(),
        'sair': lambda: exit_func(),
    }
    if value in commands_list:
        commands_list[value]()
    else:
        tasks.append(value)

    save(tasks, FILE_SAVE)

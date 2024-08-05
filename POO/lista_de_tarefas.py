# LISTA DE TAREFAS 1.0.3
import os
from time import sleep
tasks = []
checked = []


def null():  # Essa função executa quando a lista "tasks" estiver vazia.
    if not tasks:
        first = input(
            'Sua lista de tarefas está vazia, adicione algo: ').lower().strip()
        tasks.append(first)
        print(f'Lista atual: {tasks}')
        print(f'Itens concluídos: {checked}')


def add_item():

    add = input('O que quer adicionar a lista de tarefas?: ').lower().strip()
    if add not in tasks:
        tasks.append(add)


def rem_item():
    remove = input('Qual item da lista quer excluir?: ').lower().strip()
    if remove in tasks:
        index = tasks.index(remove)
        tasks.pop(index)
    else:
        print('Não tem nenhum indice com esse nome.')


def edit_item():
    edit = input('Qual item quer editar?: ')
    new_value = input('Qual a nova tarefa?: ')

    if edit in tasks:
        index = tasks.index(edit)
        tasks[index] = new_value


def check_item():
    checkin = input('Qual item quer concluir?: ')
    if checkin in tasks:
        index = tasks.index(checkin)
        value_index = tasks.pop(index)
        if value_index in checked:
            print('Item já adicionado.')
        else:
            checked.append(value_index)


def exit_program():
    return 'Programa finalizado.'


while True:

    null()
    print('Opções:')
    print('[ADD] | [REM] | [EDIT] | [CHECK] | [EXIT]')
    chose = input('Digite sua opção: ').lower().replace(' ', '')

    if chose not in ['add', 'rem', 'edit', 'check', 'exit']:
        print('Não conheço esta operação.')
        sleep(2)

    elif chose == 'add':
        add_item()

    elif chose == 'rem':
        rem_item()
        sleep(2)

    elif chose == 'edit':
        edit_item()
        sleep(2)

    elif chose == 'check':
        check_item()
        sleep(2)

    elif chose == 'exit':
        print(exit_program())
        break

    os.system('cls')
    print(f'lista atual:{tasks}')
    print(f'Itens concluídos: {checked}')

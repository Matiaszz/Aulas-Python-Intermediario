# Exercício - Salve sua classe em JSON feito
# Salve os dados da sua classe em JSON feito
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json

DIR_JSON = 'exerc_class.json'
# -----Criar Objeto-----


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


# salvar os dados
data1 = Pessoa('Allan', 17)
data2 = Pessoa('Maria', 18)
data3 = Pessoa('João', 19)
data_base = [data1.__dict__, data2.__dict__, data3.__dict__]

# importa para o json o objeto convertido em dicionario


def save_json(item, adress):
    with open(adress, 'w') as file:
        json.dump(item, file, ensure_ascii=False, indent=2)
        print('Arquivo salvo')
    return


def load_json(adress):
    with open(adress, 'r') as file:
        item = json.load(file)
    return item


load = save_json(data_base, DIR_JSON)

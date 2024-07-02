import json
import os
BASE_DIR = os.path.dirname(__file__)
JSON_FILE = os.path.join(BASE_DIR, 'Py_aula.json')

########################################################
# upar arquivos para dentro do JSON
peoples = [
    {
        'name': 'Allan',
        'surname': 'Matias',
        'age': 18,
        'ranks': ['A', 'A+'],
        'active': False,
        'telephones': {
            'residential': '11 00000-0000',
            'smartphone': '12 00000-0000',
        }

    },
    {
        'name': 'Matheus',
        'surname': 'José',
        'age': 42,
        'ranks': ['A', 'A+'],
        'active': True,
        'telephones': {
            'residential': '13 00000-0000',
            'smartphone': '14 00000-0000',
        }

    }
]

with open(JSON_FILE, 'w') as file:
    json.dump(peoples, file, indent=2)
# -------------------------------------------#
# CARREGAR ARQUIVOS DE DENTRO DO ARQUIVO JSON

with open(JSON_FILE, 'r') as file:
    peoples = json.load(file)
    print(json.dumps(peoples))
# converto um arquivo JSON para STR, primeiro eu carreguei o arquivo por meio de uma variavel, depois eu imprimi na tela essa string que esta abaixo com json.dumps(peoples)
json_str = '''
[{"name": "Allan", "surname": "Matias", "age": 18, "ranks": ["A", "A+"], "active": false, "telephones": {"residential": "11 00000-0000", "smartphone": "12 00000-0000"}},{"name": "Matheus", "surname": "Jos\u00e9", "age": 42, "ranks": ["A", "A+"], "active": true, "telephones": {"residential": "13 00000-0000", "smartphone": "14 00000-0000"}}]
'''

peoples = json.loads(json_str)

for people in peoples:
    print(people['name'])

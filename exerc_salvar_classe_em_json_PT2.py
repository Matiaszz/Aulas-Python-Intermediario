import json

from exerc_salvar_classe_em_json import DIR_JSON, Pessoa

with open(DIR_JSON, 'r') as file:
    dados = json.load(file)
    p1 = Pessoa(**dados[0])
    p2 = Pessoa(**dados[1])
    p3 = Pessoa(**dados[2])
    print(p1.nome)
    print(p2.nome)
    print(p3.nome)
# Abriu o arquivo de save, carregou os arquivos, para cada pessoa, desempacotou os dados que foram salvos (os indices foram pêgos do arq json)

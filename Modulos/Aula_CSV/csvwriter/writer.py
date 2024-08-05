import csv
from pathlib import Path

CSV_ADRESS = Path(__file__).parent / 'writer.csv'

clients = [
    {'Nome': 'Luiz Otávio', 'Endereço': 'Av 1, 22'},
    {'Nome': 'João Silva', 'Endereço': 'R. 2, "1"'},
    {'Nome': 'Maria Sol', 'Endereço': 'Av B, 3A'},
]
with open(CSV_ADRESS, 'w', encoding='utf8') as file:
    names_columns = 'Nome', 'Endereço'
    writer = csv.DictWriter(file, fieldnames=names_columns)

    writer.writeheader()

    for client in clients:
        writer.writerow(client)  # type: ignore

    # writer.writerow(clients)
# ESCREVER LISTA DE DICIONARIOS EM ARQUIVOS CSV
# with open(CSV_ADRESS, 'w', encoding='utf8') as file:

#     columns = clients[0].keys()
#     writer = csv.writer(file)
#     writer.writerow(columns)

#     for client in clients:
#         writer.writerow(client.values())

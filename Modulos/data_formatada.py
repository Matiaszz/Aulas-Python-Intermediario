from datetime import datetime

data = '2024-07-23'
fmt = '%Y-%m-%d'

data_format = datetime.strptime(data, fmt)  # cria a data

# formata a data para o jeito que vai ser exibido
print(data_format.strftime('%d/%m/%Y'))

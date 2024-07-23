# https://docs.python.org/pt-br/3.11/library/datetime.html
from datetime import datetime


data = datetime(2024, 7, 24)  # ANO | MES | DIA | (HORÁRIO FICA: 00:00:00)
print(data)

# depois do dia, vem horas, minutos e segundos.
data_tempo = datetime(2024, 7, 24, 12, 52, 59)
print(data_tempo)

str_data = '09/1/2006 13:30'
str_formato = '%d/%m/%Y %H:%M'
# %d - dia com zero a esquerda (se tiver)
# %m - mes com zero a esquerda
# %Y - Ano com zero 4 digitos
data_p = datetime.strptime(str_data, str_formato)
print(data_p)

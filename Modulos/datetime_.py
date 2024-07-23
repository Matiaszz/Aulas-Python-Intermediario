# https://docs.python.org/pt-br/3.11/library/datetime.html
# para instalar os modulos que essa aula precisa, os importse estão em
# requirements_datetime.txt

# timezones: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
from datetime import datetime
# from pytz import timezone

# data = datetime(2024, 7, 24)  # ANO | MES | DIA | (HORÁRIO FICA: 00:00:00)
# print(data)

# # depois do dia, vem horas, minutos e segundos.
# data_tempo = datetime(2024, 7, 24, 12, 52, 59)
# print(data_tempo)

# str_data = '09/1/2006 13:30'
# str_formato = '%d/%m/%Y %H:%M'
# # %d - dia com zero a esquerda (se tiver)
# # %m - mes com zero a esquerda
# # %Y - Ano com zero 4 digitos
# data_p = datetime.strptime(str_data, str_formato)
# print(data_p)

# data_now = datetime.now(timezone('America/Sitka'))  # alaska
# print(data_now)

# data_tz = datetime(2024, 7, 24, 14, 52, 59, tzinfo=timezone('Asia/Tokyo'))
# print(data_tz)

data = datetime.now()
print(data.timestamp())  # Mostra o numero de segundos desde 1/1/1970 até agora

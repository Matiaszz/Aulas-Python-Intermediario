from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

data1 = '20/05/2023 13:45:56'
data2 = '12/03/1976 09:01:23'
fmt = '%d/%m/%Y %H:%M:%S'
pdata1 = datetime.strptime(data1, fmt)
pdata2 = datetime.strptime(data2, fmt)
# delta = (pdata1 - pdata2)  # retorna um timedelta(diferença entre datas)
# print(delta.total_seconds())  # retorna segundos totais de uma data e outra
# print(delta.days)  # retorna os dias entre uma data e outra
# print(delta.seconds)  # retorna os dias entre uma data e outra
# print(delta.microseconds)  # retorna os microsegundos entre uma data e outra

deltatime = timedelta(days=10, hours=3)
print(deltatime + pdata1)  # adiciona 10 dias e 3 horas na minha data
print(relativedelta(days=10) + pdata2)  # faz a mesma coisa que o timedelta

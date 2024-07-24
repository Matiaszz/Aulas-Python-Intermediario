# 0 = segunda-feira | 6 = domingo
import calendar

# imprime o calendario do ano passado no parametro
# print(calendar.calendar(2024))

# imprime apenas o mes citado no parametro do ano citado
# print(calendar.month(2024, 4))  # parametros: ano | mes

# imprimir o ultimo dia do mes citado e do ano citado
# print(calendar.monthrange(2024, 3))

# imprime as semanas (0 = sem dia e uma lista representa uma semana)
months = calendar.monthcalendar(20204, 3)
print(*list(calendar.day_name))
counter = 1
for month in months:
    print(f's{counter}', *month)
    counter += 1

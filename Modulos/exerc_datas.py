# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


date_maria_loan = '20/12/2020'
max_loan = '20/12/2025'
value_maria_loan = 1_000_000
term_maria = 5  # anos
fmt = '%d/%m/%Y'

create_date_init = datetime.strptime(date_maria_loan, fmt)
format_date_init = create_date_init.strftime(fmt)

create_date_final = datetime.strptime(max_loan, fmt)
format_date_final = create_date_final.strftime(fmt)

month = relativedelta(months=1)
year = relativedelta(years=5)

calc_init = timedelta(create_date_init.year)
calc = create_date_init + year


installment_value = value_maria_loan / (term_maria * 12)
current = create_date_init
insatllment = []

while current <= create_date_final:
    current += month
    insatllment.append(installment_value)


print(
    f"Vencimento: {current.strftime(fmt)}, Valor: R${installment_value:.2f}")

print(
    f'Você pegou {value_maria_loan}\n',
    f'para pagar em: {len(insatllment)} parcelas\n',
    f'até {calc.year}\n',
    f'com o valor de: {installment_value:.2f} por mês.'


)

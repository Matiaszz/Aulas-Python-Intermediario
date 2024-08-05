from datetime import datetime
import locale
import string
from pathlib import Path


locale.setlocale(locale.LC_ALL, '')


def converter(num: float) -> str:
    brl = 'R$' + locale.currency(val=num, symbol=False, grouping=True)
    return brl


data = datetime(2024, 7, 30)
dados = dict(
    nome='Allan',
    valor=converter(123_456_789),
    data=data.strftime('%d/%m/%Y'),
    empresa='Fundação Casa',
    tel='+55 11 12345-6789',
)

CAMINHO = Path(__file__).parent / 'template.txt'
with open(CAMINHO, 'r', encoding='utf8') as txt:
    text = txt.read()
    template = string.Template(text)


# vai substituir os $ para a varavel declarada
print(template.substitute(dados))

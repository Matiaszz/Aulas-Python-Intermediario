import csv
from pathlib import Path

FILE_CSV = Path(__file__).parent / 'aula.csv'

with open(FILE_CSV, 'r', encoding='utf8') as file:
    # reader = csv.reader(file) # -> List
    reader = csv.DictReader(file)  # -> Dict
    for line in reader:
        print(line['Nome'])  # Posso manipular do jeito que eu quiser

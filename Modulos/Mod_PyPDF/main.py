
from pypdf import PdfReader, PdfWriter
from PyPDF2 import PdfMerger
from pathlib import Path

ROOT = Path(__file__).parent
PDF = ROOT / 'pdfs' / 'R20240802.pdf'
NEW_FILE = ROOT / 'NEW_FILES'
NEW_FILE.mkdir(exist_ok=True)

reader = PdfReader(PDF)
pages = reader.pages

# print(page.extract_text())


# Salvar imagens na pasta NEW_FILES
# count = 0
# for img in page.images:
#     with open(NEW_FILE / f'{img.name}', 'wb') as fp:
#         fp.write(img.data)
#         count += 1

# writer = PdfWriter()


# with open(NEW_FILE / 'NOVOPDF.pdf', 'wb', ) as file:
#     for page in pages:
#         writer.add_page(page)
#     writer.write(file)


# para cada pagina de um pdf, cria um pdf separado
for i, page in enumerate(pages):
    writer = PdfWriter()
    with open(NEW_FILE / f'Outropdf{i}.pdf', 'wb') as file:
        writer.add_page(page)
        writer.write(file)


files = [
    NEW_FILE / 'Outropdf1.pdf',
    NEW_FILE / 'Outropdf0.pdf',
]

merg = PdfMerger()

for file in files:
    merg.append(file)

with open(NEW_FILE / 'Arquivo_Juntado.pdf', 'wb') as file:
    merg.write(file)

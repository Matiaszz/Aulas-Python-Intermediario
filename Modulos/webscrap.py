import requests
from bs4 import BeautifulSoup

url = 'http://localhost:3000/'
response = requests.get(url)
raw_html = response.text  # retorna o html
# torna possivel o webscrap
parsed_html = BeautifulSoup(raw_html, 'html.parser')


# if parsed_html.article is not None:
#     print(parsed_html.article.text)

# Pega o texto "Top jobs do site"
top_jobs = parsed_html.select_one('#intro > div > div > article > h2')

# verifica se top jobs foi passado algo
if top_jobs is not None:
    parent = top_jobs.parent  # pega o elemento pai do H2 que o top jobs está
    print(top_jobs.text)
    if parent is not None:
        # pega todos os  P's do HTML que estiver dentro do elemento pai
        for p in parent.select('p'):
            print(p.text)

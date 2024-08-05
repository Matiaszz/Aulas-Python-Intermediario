import requests

# http:// -> porta 80 padrão
# https:// -> porta 443 padrão
url = 'http://localhost:3000/'

# verifica se é possivel fazer a conexão com o site
response = requests.get(url)
print(response.status_code)  # -> 200 (sucesso)
print(response.text)  # retorna o codigo HTML

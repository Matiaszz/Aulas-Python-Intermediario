# NUNCA MANDAR REPOSITORIO COM .env


# import os
# # $env:SENHA="VALOR QUE EU QUERO"
# print(os.getenv('SENHA'))  # -> O VALOR DA VARIAVEL ACIMA
import os
from dotenv import load_dotenv

load_dotenv()
# print(os.environ) #me da um dicionario com todas as variaveis de ambiente
print(os.getenv('BD_USER'))

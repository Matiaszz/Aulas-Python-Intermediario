# NÃO USAR ESSE MODULO PARA SEGURANÇA EM GERAL (criptografia por exemplo)
import random

# random.seed(0) # Define a PSEUDOALEATORIEDADE do codigo

# gera um numero aleatorio entre 10 e 20  com step de 2
r_range = random.randrange(10, 20, 2)
print('Randrange:', r_range)

r_randint = random.randint(10, 20)  # numero aleatorio INTEIRO entre 10 e 20
print('Randint:', r_randint)

r_uniform = random.uniform(10, 20)   # numero aleatorio FLOAT entre 10 e 20
print(f'Uniform (float): {r_uniform:.2f}')

lista = ['Allan', 'Matheus', 'Maria', 'Helena', 'João']
# random.shuffle(lista)  # embaralha a lista original

# imprime um trecho da lista (k sendo a quantidade de valores que voce quer)
nova_lista = random.sample(lista, k=2)

# mesma coisa do sample, porém pode repitir um valor
r_choices = random.choices(lista, k=2)

# pega um valor aleatorio da minha lista
r_choice = random.choice(lista)

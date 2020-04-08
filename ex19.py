#  Altere o programa anterior para que ele aceite apenas números entre 0 e 1000

from random import randint

conjunto = []

for x in range(0,10):
    conjunto.append(randint(0, 1000))
    
print(conjunto)
print(f'O menor valor do conjunto {min(conjunto)}')
print(f'O maior valor do conjunto {max(conjunto)}')
print(f'A soma do conjunto é igual a {sum(conjunto)}')
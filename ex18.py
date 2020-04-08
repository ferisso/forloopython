# Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos
# valores
from random import randint

conjunto = []

for x in range(0,10):
    conjunto.append(randint(0, 10))
    
print(conjunto)
print(f'O menor valor do conjunto {min(conjunto)}')
print(f'O maior valor do conjunto {max(conjunto)}')
print(f'A soma do conjunto é igual a {sum(conjunto)}')
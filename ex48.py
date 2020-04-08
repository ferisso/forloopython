# Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido

n = int(input('> '))
lista_n = []

for x in range(1, n+1):
    lista_n.append(x)

print(*lista_n, sep=" ")

lista_n.reverse()

print(*lista_n, sep=" ")
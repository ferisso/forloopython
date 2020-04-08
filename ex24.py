# Faça um programa que calcule o mostre a média aritmética de N notas.

n = int(input('> '))
notas = []

for x in range(1 , n + 1):
    notas.append(float(input('Notas: ')))

print(f'A média é igual a {sum(notas) / len(notas)}')
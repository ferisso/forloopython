# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo
# compreendido por eles

x = int(input('> '))
y = int(input('> '))

for x in range(x, y + 1):
    print(x)
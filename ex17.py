# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

n = int(input('Escolha um numero fatorial: '))
fatorial = 1

for x in range(1, n + 1):
    fatorial = fatorial * x
    print(fatorial)
print(f'O resultado é: {fatorial}')
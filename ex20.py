# Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a
# números inteiros positivos e menores que 16.

n = int(input('Escolha um numero fatorial: '))
fatorial = 1

while n > 15 or n < 0:
    n = int(input('Escolha um numero fatorial: '))

for x in range(1, n + 1):
    fatorial = fatorial * x
    print(fatorial)
print(f'O resultado é: {fatorial}')
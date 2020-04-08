# Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao
# segundo número. Não utilize a função de potência da linguagem.

n1 = int(input('Base: '))
n2 = int(input('Potencia: '))
potencia = n1

for x in range(1, n2 + 1):
    potencia = potencia * n1
    print(potencia)


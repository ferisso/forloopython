# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A
# saída deve ser conforme o exemplo abaixo:

n = int(input('Escolha um numero fatorial: '))
fatorial = 1
fatorial_lista = []

for x in range(1, n + 1):
    fatorial = fatorial * x
    fatorial_lista.append(x)

fatorial_lista.reverse()

print(f'O fatorial de: {n}')
print(*fatorial_lista, sep=" . ", end= f' = {fatorial}')

#  Altere o programa anterior para mostrar no final a soma dos números

x = int(input('> '))
y = int(input('> '))
soma = 0

for x in range(x, y + 1):
    soma = x + soma
    print(x)

print(soma)
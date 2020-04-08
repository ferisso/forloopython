n = int(input('Qual termo da sequecia de Fibonacci que saber:  '))
anterior = 0
proximo = 1

print('termo 1 = 1')

for x in range(1, n):
    proximo = proximo + anterior
    anterior = proximo - anterior
    print(f'termo {x + 1} = {proximo}')

print(f'O termo de numero {n} na sequencia de Fibonacci é o: {proximo}')

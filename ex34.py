# Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número
# primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e
# determine se ele é ou não um número primo

n = int(input('> '))
primo = []

for x in range(1, n + 1):
    seletor = n / x
    if seletor == int(seletor):
        primo.append(seletor)

if len(primo) == 2:
    print(f'O numero {n} é primo')  
else:
    print(f'O numero {n} não é primo')
    print(f'Ele é divisivel por {primo}')
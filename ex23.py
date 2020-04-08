# Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O
# programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.
# Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

n = int(input('> '))
primo = []

for x in range(1, n + 1):
    seletor = n / x
    print(f'{n} / {x} = {seletor}')
    if seletor == int(seletor):
        primo.append(seletor)

print(30*'==')
print(f'O numero de divisões efetuadas foi {n}')

if len(primo) == 2:
    print(f'O numero {n} é primo')  
else:
    print(f'O numero {n} não é primo')
    print(f'Ele é divisivel por {primo}')
# Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número
# ele é divisível.

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
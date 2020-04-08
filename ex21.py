# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é
# aquele que é divisível somente por ele mesmo e por 1.

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
    
   
    
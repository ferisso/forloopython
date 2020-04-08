#  Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade
# de números impares

lista_impar = []
lista_par = []

for x  in range(0,10):
    num = int(input('> '))
    if num % 2 == 1:
        lista_impar.append(num)
    else:
        lista_par.append(num)

print(f'numeros pares: {len(lista_par)}')
print(f'numeros impares: {len(lista_impar)}')

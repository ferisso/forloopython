# Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade
# da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a
# média calculada.

n = int(input('Quantas pessoas tem nesse grupo:  '))
notas = []

for x in range(1 , n + 1):
    notas.append(int(input('Idade das pessoas: ')))

media = sum(notas) / len(notas)

if media < 26:
    print(f'A idade media foi de {media}')
    print('Podemos considerar o grupo jovem')
elif media > 26 and media < 60:
    print(f'A idade media foi de {media}')
    print('Podemos considerar o grupo adulto')
elif media > 60:
    print(f'A idade media foi de {media}')
    print('Podemos considerar o grupo idoso')
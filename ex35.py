# Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a
# tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados
# também pelo usuário, conforme exemplo abaixo:

escolha = int(input('Escolha uma tabuada: '))
inicio = int(input('Comecar a tabuada em: '))
final = int(input('Terminar a tabuada em:  '))
tabuada = 0 

while final < inicio:
    print('O final nao pode ser menor que o incio')
    final = int(input('Terminar a tabuada em:  '))

for x in range(inicio, final + 1):
    tabuada = x * escolha
    print(f'Tabuada do {escolha}: ')
    print(f'{escolha} X {x} = {tabuada}')
#  Faça um programa que peça uma nota, entre zero e dez.
#  Mostre uma mensagem caso o valor seja inválido e
#  continue pedindo até que o usuário informe um valor válido.

nota = int(input('Insira a nota: '))

while nota < 0 or nota > 11:
    print('Insira uma nota valida:')
    nota = int(input('Insira a nova nota: '))

print('Nota valida')

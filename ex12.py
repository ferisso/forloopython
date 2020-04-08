# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário
# deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:

escolha = int(input('> '))
tabuada = 0 

for x in range(1, 11):
    tabuada = x * escolha
    print(f'Tabuada do {escolha}: ')
    print(f'{escolha} X {x} = {tabuada}')

# Faça um programa que leia e valide as seguintes informações:
# a. Nome: maior que 3 caracteres;
# b. Idade: entre 0 e 150;
# c. Salário: maior que zero;
# d. Sexo: 'f' ou 'm';
# e. Estado Civil: 's', 'c', 'v', 'd';

nome = ''
idade = 0
salario = 0
sexo = ''
estado_civil = ''

while len(nome) <= 4:
    print('Insira um nome com no minimo 4 caracteres: ')
    nome = input('Insira o nome: ')

while idade <= 0 or idade > 149:
    print('Insira sua idade')
    idade = int(input('Insira a sua idade: '))

while salario < 0:
    print('Insira um salario maior que 0')
    salario = int(input('Salario: '))

while sexo.lower() != 'f' and sexo.lower() != 'm':
    print('Insira o seu Sexo')
    sexo = input('Qual o seu sexo insira M ou F: ')
    
while estado_civil.lower() != 's' and estado_civil.lower() != 'c' and estado_civil.lower() != 'v' and estado_civil.lower() != 'd':
    print('Insira o seu Estado Civil')
    estado_civil = input('Qual o seu estado civil: (S)olteiro, (C)asado, (V)iuvo, (D)ivorciado ')

print('sucesso')


# Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o
# segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número
# do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.

codigo = []
altura = []

for x in range(1, 11):
    codigo.append(str(input('Insira o codigo do aluno: ')))
    altura.append(int(input('Insira a altura do aluno: ')))

baixo = altura.index(min(altura))
alto =  altura.index(max(altura))

print(f'Aluno mais baixo = Codigo: {codigo[baixo]} com altura de {min(altura)} cm')
print(f'Aluno mais alto = Codigo: {codigo[alto]} com altura de {max(altura)} cm')
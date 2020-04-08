# Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a
# quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.

turmas = int(input('> '))
alunos = []

for x in range(1, turmas + 1):
    alunos.append(int(input('Numero de alunos por turma: ')))
    while alunos[-1] > 40:
        print('Erro o numero maximo de alunos na sala e de 40. Insira novamente: ')
        alunos.pop(-1)
        alunos.append(int(input('Numero de alunos por turma: ')))
    print(alunos)

print(f'A media de alunos por turma: {sum(alunos) / len(alunos)}')
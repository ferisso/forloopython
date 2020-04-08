# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada
# eleitor votar e ao final mostrar o número de votos de cada candidato.

eleitores = int(input('Numero de eleitores: '))
count_1 = 0
count_2 = 0
count_3 = 0

for x in range(1, eleitores + 1):
    votos = int(input('Aperte 1 e confirme para votar no candidato 1, Aperte 2 e confirme para votar no candidato 2, Aperte 3 e confirme para votar no candidato 3: '))
    if votos == 1:
        count_1 = count_1 + 1
    elif votos == 2:
        count_2 = count_2 + 1
    elif votos == 3:
        count_3 = count_3 +1

print(f'O numero de votos do candidato 1 foi de : {count_1}')
print(f'O numero de votos do candidato 2 foi de : {count_2}')
print(f'O numero de votos do candidato 3 foi de : {count_3}')
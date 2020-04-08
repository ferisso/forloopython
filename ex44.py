# Faça um programa que calcule e mostre:
# O total de votos para cada candidato;
# O total de votos nulos;
# O total de votos em branco;
# A percentagem de votos nulos sobre o total de votos;
# A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero

possiveis_votos = [1, 2, 3, 4, 5, 6]
candidatos = ['Candidato 1', 'candidato 2', 'Candidato 3', 'Candidato 4', 'Nulo', 'Branco']
votos = []

voto = True
n_votos = 1
while voto != 0:
    print("Voto n°", n_votos)
    voto = int(input("Digite o seu voto: "))
    if voto == 0:
        break
    else:
        while voto not in possiveis_votos:
            print("[Voto invalido.]")
            voto = int(input("Digite o seu voto: "))
        votos.append(voto)
    n_votos += 1

contador = 0
print("\n" * 2)
for i in range(len(candidatos)):
    print("Votos para ", candidatos[contador], end=" : ")
    if votos.count == 0:
        print("0")
        contador += 1
    else:
        print(votos.count(contador + 1))
        contador += 1

porcentagem_nulo = (votos.count(5) / len(votos)) * 100
porcentagem_branco = (votos.count(6) / len(votos)) * 100
print("\nPorcentagem Nulos: ", round(porcentagem_nulo, 2), "%\nPorcentagem Brancos: ", round(porcentagem_branco, 2),"%")
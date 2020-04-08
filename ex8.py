#  Faça um programa que leia 5 números e informe a soma e a média dos números.

valores = []
for x in range(5):
    valores.append(float(input('> ')))

media = sum(valores) / len(valores)

print(media)
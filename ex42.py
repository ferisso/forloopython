# Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles e
# stão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.

n25 = []
n50 = []
n75 = []
n100 = []
numero = True
while numero > 0:
    numero = int(input("Digite um número: "))
    if numero > 0 and numero <= 25:
        n25.append(numero)
    elif numero > 25 and numero <= 50:
        n50.append(numero)
    elif numero > 50 and numero <= 75:
        n75.append(numero)
    elif numero > 75 and numero <= 100:
        n100.append(numero)

print("\n[0, 25]: ", len(n25))
print("[26, 50]: ", len(n50))
print("[51, 75]: ", len(n75))
print("[76, 100]: ", len(n100))
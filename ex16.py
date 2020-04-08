#  A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até
# que o valor seja maior que 500.

proximo = 1
anterior = 0

while proximo < 500:
    print(proximo)
    proximo = proximo + anterior
    anterior = proximo - anterior
    
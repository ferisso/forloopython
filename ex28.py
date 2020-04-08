# Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio
# gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.

qntd_cd = int(input("Quantidade de CD's: "))
ncd = 0
cd =[]

for x in range(1, qntd_cd + 1):
    ncd = ncd + 1
    cd.append(int(input(f'Valor do cd {ncd}: ')))

print(f"O total gato com CD's foi de {sum(cd)}")
print(f'Valor medio de cada CD e: {sum(cd)/len(cd)}')
    

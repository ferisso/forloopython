# O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto
# indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média
# das temperaturas.

temperaturas = int(input('Quantas temperaturas deseja registrar:  '))
temperatura_lista = []

for x in range(1, temperaturas + 1):
    temperatura_lista.append(int(input(f'Temperatura {x}: ')))
   
print(f'A maior temperatura foi de: {max(temperatura_lista)}')
print(f'A menor temperatura foi de: {min(temperatura_lista)}')
print(f'A media de temperatura foi de: {sum(temperatura_lista) / len(temperatura_lista)}')
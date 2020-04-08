# Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos
# os seguintes dados:
# a. Código da cidade;
# b. Número de veículos de passeio (em 1999);
# c. Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
# =====================================================================================================================
# d. Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
# e. Qual a média de veículos nas cinco cidades juntas;
# f. Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio

codigo = []
num_veiculos = []
num_acidentes = []
cidade_veiculos = []

for x in range(1, 2):
    codigo.append(str(input('Insira o codigo da  cidade: ')))
    num_veiculos.append(int(input(f'Inisra o numero de veiculos da cidade {codigo[-1]}: ')))
    num_acidentes.append(int(input(f'insira o numero de acidentes da cidade {codigo[-1]} : ')))

menor_indice = num_acidentes.index(min(num_acidentes))
maior_indice = num_acidentes.index(max(num_acidentes))

print(f'O menor indice de acidentes pertence a cidade com o codigo {codigo[menor_indice]} com apenas {min(num_acidentes)} acidentes')
print(f'O maior indice de acidentes pertence a cidade com o codigo {codigo[maior_indice]} com {max(num_acidentes)} acidentes')
print(f'A media de veiculos nas 5 cidades: {sum(num_veiculos) / len(num_veiculos)}')

for y in num_veiculos:
    if y < 2000:
        cidade_veiculos.append(y)

print(f'A media de veiculos das cidades com menos de 2000 foi de {sum(cidade_veiculos) / len(cidade_veiculos)}')
# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a
# entrada e permita repetir a operação.

pais_a = 80000
pais_b = 200000
anos = 0 
taxa_a = float(input('Taxa de crescimento pais A: ')) / 100 + 1
taxa_b = float(input('Taxa de crescimento pais B: ')) / 100 + 1

while pais_a < pais_b:
    anos = anos + 1
    pais_a = pais_a * taxa_a
    pais_b = pais_b * taxa_b
    print(anos)

print(f'Foram necessarios {anos} anos')
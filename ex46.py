# Em uma competição de salto em distância cada atleta tem direito a cinco saltos. No final da série de saltos de cada
# atleta, o melhor e o pior resultados são eliminados. O seu resultado fica sendo a média dos três valores restantes.
# Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e
# depois informe a média dos saltos conforme a descrição acima informada (retirar o melhor e o pior salto e depois
# calcular a média). Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da
# execução, portanto não são ordenados. O programa deve ser encerrado quando não for informado o nome do
# atleta. A saída do programa deve ser conforme o exemplo abaixo:

nome_atleta = True
n_atleta = 1
while nome_atleta != '':
    saltos = []
    print("\n" * 5)
    print("Atleta n°", n_atleta)
    nome_atleta = input("Digite o nome do atleta: ")
    if nome_atleta == '':
        break
    else:
        n_salto = 1
        print("\n" * 3)
        for i in range(5):
            print("Salto n° ", n_salto)
            distancia_salto = float(input("Digite a distancia do salto: "))
            saltos.append(distancia_salto)
            n_salto += 1
        print("Atleta: ", nome_atleta)
        n_salto = 1
        count = 0
        for i in range(5):
            print(n_salto, "° salto : ", saltos[count]," m")
            n_salto += 1
            count += 1
        print("Melhor salto: ", max(saltos), " m")
        print("Pior salto: ", min(saltos), " m")

        saltos.remove(max(saltos))
        saltos.remove(min(saltos))
        media = sum(saltos) / len(saltos)
        print("Media dos demais saltos: ", round(media, 2))
        print("Resultado Final: \n", nome_atleta, " : ", round(media, 2))
        n_atleta += 1
# O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de
# conveniências. Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber
# um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser informado
# pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o valor
# em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o programa
# deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:

preco = []
produto = 1

preco.append(int(input('Valor do produto: ')))
print(f'Produto {produto} : R$ {preco[-1]}')

while preco[-1] != 0:
    preco.append(int(input('Valor do proximo produto: ')))
    produto = produto + 1
    print(f'Produto {produto} : R$ {preco[-1]}')

total = sum(preco)
print(f'Total: {total}')
dinheiro = int(input('Dinheiro: R$ '))

if dinheiro > total:
    troco = dinheiro - total
    print(f'Total: R$ {total}')
    print(f'Troco: R$ {troco}')
elif dinheiro == total:
    troco = dinheiro - total
    print(f'Total: R$ {total}')
    print(f'Troco: R$ {troco}')
elif dinheiro < total:
    troco = dinheiro - total
    print('Erro dinheiro Insuficiente.')
    




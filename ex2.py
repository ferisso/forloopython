# Faça um programa que leia um nome de usuário e
# a sua senha e não aceite a senha igual ao nome do usuário,
# mostrando uma mensagem de erro e voltando a pedir as informações.

username = input('Insira o seu nome de usuario: ')
password = input('Insira sua senha: ')

while username == password:
    print('O usuario e a senha nao podem ser iguais')
    password = input('Insira uma nova senha: ')

print('Cadastro realizado com sucesso')
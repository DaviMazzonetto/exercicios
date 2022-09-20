# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
#  mostrando uma mensagem de erro e voltando a pedir as informações.

def plumbus(nome:str, senha:str):
    return nome!=senha
  
while (True):
    nome = input('Digite seu nome de usuário:')
    senha = input('Digite sue senha:')

    if plumbus (nome, senha):
        print('Cadastro efetuado.')
        break
    


   



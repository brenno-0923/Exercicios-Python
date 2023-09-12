# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
nome = input("Seu nome:\n")
senha = input("Sua senha:\n")

while (nome == senha):
  print("ERRO!")
  nome = input("Seu nome:\n")
  senha = input("Sua senha:\n")
else:
  print("Nome e senha validados!")


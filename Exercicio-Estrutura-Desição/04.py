#	Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#	"Telefonou para a vítima?"
#	"Esteve no local do crime?"
#	"Mora perto da vítima?"
#	"Devia para a vítima?"
#	"Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

pergunta1 = (input("Telefonou para a vítima?"))
pergunta2 = (input("Esteve no local do crime?"))
pergunta3 = (input("Mora perto da vítima?"))
pergunta4 = (input("Devia para a vítima?"))
pergunta5 = (input("Já trabalhou com a vítima?"))

resposta = [pergunta1,pergunta2,pergunta3,pergunta4,pergunta5]
contador = resposta.count("s")

if contador == 2:
  print("Suspeita")
elif contador == 3 or contador == 4:
  print("Cúmplice")
elif contador == 5:
  print("Assassino")
else:
  print("inocente")
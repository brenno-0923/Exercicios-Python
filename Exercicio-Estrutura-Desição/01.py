#Faça um Programa que peça dois números e imprima o maior deles.
num1 = int(input("Informe um numero:"))
num2 = int(input("Informe mais um numero:"))
if num1 > num2:
  print("{} é o maior numero".format(num1,num2))
else:
  print("{} é o maior numero".format(num2,num1))
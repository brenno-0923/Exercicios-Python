# Faça um programa que leia 5 números e informe a soma e a média dos números.

soma = 0
for x in range(5):
  nota=float(input("Informe uma nota:"))
  soma += nota

media = soma / 5

print(media)
# Faça um programa que leia um numero inteiro e diga se ele é ou não um número primo.

numero = int(input("Digite um número: "))
cont = 0
for i in range(1, numero + 1):
    if numero % i == 0:
        cont += 1
if cont == 2:
    print(f"{numero} é primo")
else:
    print(f"{numero} não é primo")
print("FIM")
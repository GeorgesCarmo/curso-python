# Faça um programa que solicite um numero ao usuário e mostre na tela a tabuada desse número.
numero = int(input("Digite um número: "))
print(f"Tabuada do {numero}")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
print("FIM")
# Estrutura de repetição for
from time import sleep

for counter in range(1, 11):
    print(counter)
print("FIM")

for counter in range(1, 11, 2):
    print(counter)
print("FIM")

for counter in range(5, 0, -1):
    print(counter)
    sleep(1)
print("FIM")

numero = int(input("Digite um número: "))
for counter in range(0, numero + 1):
    print(counter)
print("FIM")

inicio = int(input("Digite o início: "))
fim = int(input("Digite o fim: "))
passo = int(input("Digite o passo: "))
for counter in range(inicio, fim + 1, passo):
    print(counter)
print("FIM")

somatorio = 0
for counter in range(1, 6):
    numero = int(input("Digite um número: "))
    somatorio += numero
print(f"A soma dos números é {somatorio}")
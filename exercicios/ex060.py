# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar 999, que é a condição de parada. 
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

print("=" * 20)
print("SOMA DOS NÚMEROS")
print("=" * 20)
soma = 0
cont = 0
while True:
    n = int(input("Digite um número (999 para parar): "))
    if n == 999:
        break
    soma += n
    cont += 1
print(f"A soma dos {cont} números é {soma}.")
print("Programa encerrado.")
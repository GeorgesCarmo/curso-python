# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

contador = somador = 0
while True:
    numero = int(input("Digite um número: "))
    if numero == 999:
        break
    contador += 1
    somador += numero
print(f"A soma dos {contador} números digitados foi {somador}")
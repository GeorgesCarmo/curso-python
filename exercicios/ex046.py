# Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
somador = 0
cont = 0
for n in range(1, 7):
    numero = int(input(f"Digite o {n}º número: "))
    if numero % 2 == 0:
        somador += numero
        cont += 1
print(f"A soma dos {cont} números pares é {somador}")
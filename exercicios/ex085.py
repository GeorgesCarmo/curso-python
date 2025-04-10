# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha os valores pares e ímpares separados. 
# No final, mostre os valores pares e ímpares em ordem crescente.

valores = []
pares = []
impares = []
for i in range(7):
    valor = int(input(f'Digite o {i+1}º valor: '))
    valores.append(valor)
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
pares.sort()
impares.sort()
print(f'A lista completa é: {valores}')
print(f'Os valores pares são: {pares}')
print(f'Os valores ímpares são: {impares}')
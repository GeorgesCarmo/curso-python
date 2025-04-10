# Crie um programa que vai ler vário números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter 
# apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

numeros = []
pares = []
impares = []
while True:
    num = int(input('Digite um número: '))
    numeros.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Foram digitados {len(numeros)} valores.')
print(f'Os valores digitados foram: {numeros}')
print(f'Os valores pares foram: {pares}')
print(f'Os valores ímpares foram: {impares}')
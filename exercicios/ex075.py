# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# a) Quantas vezes apareceu o valor 9.
# b) Em que posição foi digitado o primeiro valor 3.
# c) Quais foram os numeros pares.

numeros = (int(input('Digite um número: ')),
    int(input('Digite outro número: ')),
    int(input('Digite mais um número: ')),
    int(input('Digite o ultimo número: ')))
print(f'Os números digitados foram: {numeros}')
print(f'O número 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O primeiro número 3 foi digitado na posição {numeros.index(3) + 1}')
else:
    print('O número 3 não foi digitado')
print('Os números pares digitados foram: ', end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')
print()
# Crie um programa que leia vários números e coloque em uma lista. Depois disso, mostre:
# a) Quantos números foram digitados.
# b) A lista de valores ordenada de forma decrescente.
# c) Se o valor 5 foi digitado e esta na lista.

valores = []
while True:
    num = int(input('Digite um número: '))
    valores.append(num)
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Foram digitados {len(valores)} valores.')
valores.sort(reverse=True)
print(f'Os valores digitados em ordem decrescente: {valores}')
if 5 in valores:
    print('O valor 5 foi digitado e está na lista.')
else:
    print('O valor 5 não foi digitado e não está na lista.')
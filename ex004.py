# Crie um algoritimo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
num = int(input('Digite um número: '))
print('O dobro de {} é {}, o triplo é {} e a raiz quadrada é {:.2f}'.format(num, num * 2, num * 3, num ** (1/2)))

print('-' * 50)

# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a média.
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print('A média entre {} e {} é: {:.2f}'.format(n1, n2, media))

print('-' * 50)

# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
m = float(input('Digite um valor em metros: '))
print('O valor em centímetros é: {} cm'.format(m * 100))
print('O valor em milímetros é: {} mm'.format(m * 1000))

print('-' * 50)

# Escreva um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.
num = int(input('Digite um número inteiro: '))
if num % 2 == 0:
    print('O número {} é par'.format(num))
else:
    print('O número {} é ímpar'.format(num))

print('-' * 50)

# Escreva um programa que leia um número inteiro e mostre na tela se ele é positivo ou negativo.
num = int(input('Digite um número inteiro: '))
if num >= 0:
    print('O número {} é positivo'.format(num))
else:
    print('O número {} é negativo'.format(num))

print('-' * 50)
    
# Escreva um programa que leia um número inteiro e mostre na tela se ele é primo ou não.
num = int(input('Digite um número inteiro: '))
cont = 0
for c in range(1, num + 1):
    if num % c == 0:
        cont += 1
if cont == 2:
    print('O número {} é primo'.format(num))
else:
    print('O número {} não é primo'.format(num))
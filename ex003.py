name = input('Qual é o seu nome? ')
print('Prazer em te conhecer, {:>20}!'.format(name))
print('Prazer em te conhecer, {:->20}!'.format(name))
print('Prazer em te conhecer, {:<20}!'.format(name))
print('Prazer em te conhecer, {:^20}!'.format(name))
print('Prazer em te conhecer, {:-^20}!'.format(name))

print('=' * 20)

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
print('A soma é {}, a multiplicação é {}, a divisão é {:.2f}'.format(num1 + num2, num1 * num2, num1 / num2), end=' ')
print('A subtração é {}, o resto da divisão é {}, a média é {:.2f}'.format(num1 - num2, num1 % num2, (num1 + num2) / 2))
print('A divisão inteira é {}, a potência é {}'.format(num1 // num2, num1 ** num2))

print('=' * 20)

# Desafio: faça um programa que leia um número inteiro e mostre na tela seu sucessor e seu antecessor.
num = int(input('Digite um número: '))
print('O sucessor de {} é {}, e o antecessor é {}'.format(num, num + 1, num - 1))

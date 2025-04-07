# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiro elementos de uma Sequência de Fibonacci.

# Exemplo:
# 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

n = int(input("Quantos termos você quer mostrar? "))
a = 0
b = 1
c = 0
print("Sequência de Fibonacci:")
print(f"{a} -> {b}", end=" -> ")
if n > 2:
    for i in range(2, n):
        c = a + b
        print(c, end=" -> ")
        a = b
        b = c
print("ACABOU")
# Desenvolva um programa que leia o comprimeiro de 3 retas e diga ao usuário se elas podem ou não formar um triângulo.
# O programa deve perguntar o comprimento de cada reta e verificar se a soma de dois lados é maior que o terceiro lado.
# Se sim, formam um triângulo, se não, não formam.
r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('As retas podem formar um triângulo!')
else:
    print('As retas não podem formar um triângulo!')

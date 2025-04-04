# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.
nome = input('Qual é o seu nome completo? ').strip()
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))
# Outra forma de fazer
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper().split()))
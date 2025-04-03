# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida
# - O primeiro e o último nome separadamente.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.
# - Quantas letras tem o último nome.
nome = input('Qual é o seu nome completo? ').strip()
nome = nome.split()
print('Analisando seu nome...')
print(f'Seu primeiro nome é {nome[0]} e o seu último nome é {nome[-1]}')
print(f'Seu primeiro nome é {nome[0]} e ele tem {len(nome[0])} letras')
print(f'Seu último nome é {nome[-1]} e ele tem {len(nome[-1])} letras')
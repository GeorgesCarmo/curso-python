# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda nao atingiram a maioridade e quantas ja sao maiores.
from datetime import date
ano_atual = date.today().year
maioridade = 0
menoridade = 0
for c in range(1, 8):
    ano_nascimento = int(input(f"Em que ano a {c}ª pessoa nasceu? "))
    idade = ano_atual - ano_nascimento
    if idade >= 18:
        maioridade += 1
    else:
        menoridade += 1
print(f"Total de pessoas maiores de idade: {maioridade}")
print(f"Total de pessoas menores de idade: {menoridade}")
# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
# A) Qual é o total gasto na compra.    
# B) Quantos produtos custam mais de R$1000.
# C) Qual é o nome do produto mais barato.

totalGasto = produtosMais1000 = 0
maisBarato = ' '
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço do produto: R$'))
    totalGasto += preco
    if preco > 1000:
        produtosMais1000 += 1
    if maisBarato == ' ' or preco < precoMaisBarato:
        maisBarato = produto
        precoMaisBarato = preco
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'Total gasto na compra: R${totalGasto:.2f}')
print(f'Temos {produtosMais1000} produtos custando mais de R$1000.')
print(f'O produto mais barato foi {maisBarato} que custa R${precoMaisBarato:.2f}.')
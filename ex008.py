# Faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco = float(input('Digite o preço do produto: R$'))
desconto = 5
novo_preco = preco - (preco * desconto / 100)
print('O novo preço do produto com {}% de desconto é: R${:.2f}'.format(desconto, novo_preco))
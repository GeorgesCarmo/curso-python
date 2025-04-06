# Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela nao pode exceder 30% do salario ou entao o emprestimo sera negado.
casa = float(input('Qual é o valor da casa? '))
salario = float(input('Qual é o seu salario? '))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação mensal sera de R${:.2f}'.format(casa, anos, prestacao))
if prestacao <= minimo:
    print('Emprestimo aprovado!')
else:
    print('Emprestimo negado!')
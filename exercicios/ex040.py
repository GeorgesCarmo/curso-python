# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - À vista dinheiro/cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros
preco = float(input('Qual é o preço do produto? R$'))
print('Escolha a condição de pagamento:')
print('[1] a vista dinheiro/cheque')
print('[2] a vista no cartão')
print('[3] 2x no cartão')
print('[4] 3x ou mais no cartão')
opcao = int(input('Qual é a opção escolhida? '))
if opcao == 1:
    desconto = preco * 10 / 100
    preco_final = preco - desconto
    print('O preço final com 10% de desconto é R${:.2f}'.format(preco_final))
elif opcao == 2:
    desconto = preco * 5 / 100
    preco_final = preco - desconto
    print('O preço final com 5% de desconto é R${:.2f}'.format(preco_final))
elif opcao == 3:
    preco_final = preco
    print('O preço final sem desconto é R${:.2f}'.format(preco_final))
elif opcao == 4:
    juros = preco * 20 / 100
    preco_final = preco + juros
    print('O preço final com 20% de juros é R${:.2f}'.format(preco_final))
else:
    print('Opção inválida! Tente novamente.')
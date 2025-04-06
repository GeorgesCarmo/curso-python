# Escreva um programa que leia um numero inteiro qualquer e peça para o usuario escolher qual sera a base de conversao:
# 1 para binario
# 2 para octal
# 3 para hexadecimal
# Exiba o resultado da conversao na tela.

numero = int(input('Digite um numero inteiro: '))
print('Escolha uma das bases para conversao:')
print('[1] converter para binario')
print('[2] converter para octal')
print('[3] converter para hexadecimal')
opcao = int(input('Sua opcao: '))
if opcao == 1:
    print('O numero {} convertido para binario é igual a {}'.format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('O numero {} convertido para octal é igual a {}'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('O numero {} convertido para hexadecimal é igual a {}'.format(numero, hex(numero)[2:]))
else:
    print('Opção invalida! Tente novamente.')
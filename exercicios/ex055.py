# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] Somar
# [2] Multiplicar
# [3] Maior
# [4] Novos Números
# [5] Sair do Programa
# Seu programa deverá realizar a operação solicitada em cada caso.

opcao = 0
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
while opcao != 5:
    print('''
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Números
    [5] Sair do Programa
    ''')
    opcao = int(input('Qual é a opção escolhida? '))
    if opcao == 1:
        print('A soma entre {} e {} é igual a {}'.format(n1, n2, n1 + n2))
    elif opcao == 2:
        print('A multiplicação entre {} e {} é igual a {}'.format(n1, n2, n1 * n2))
    elif opcao == 3:
        if n1 > n2:
            print('O maior entre {} e {} é {}'.format(n1, n2, n1))
        elif n1 == n2:
            print('Os dois números são iguais')    
        else:
            print('O maior entre {} e {} é {}'.format(n1, n2, n2))
    elif opcao == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
print('Fim do programa. Volte sempre!')    
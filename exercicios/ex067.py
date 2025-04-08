# Crie um programa que simule o funcionamento de um caixa eletronico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão fornecidas.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
print('=' * 30)
print('{:^30}'.format('BANCO PYTHON'))
print('=' * 30)
while True:
    saque = int(input('Quanto deseja sacar? '))
    cedula = 50
    notas = 0
    while True:
        if saque >= cedula:
            saque -= cedula
            notas += 1
        else:
            if notas > 0:
                print(f'{notas} nota(s) de R${cedula}')
            if cedula == 50:
                cedula = 20
            elif cedula == 20:
                cedula = 10
            elif cedula == 10:
                cedula = 1
            notas = 0
            if saque == 0:
                break
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('Obrigado por usar nosso caixa eletrônico!')
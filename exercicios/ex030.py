# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# O aumento deverá ser de 15% se o salário for abaixo de R$ 1.250,00, caso contrário, será de 10%.
salario = float(input('Qual é o salário do funcionário? R$ '))
if salario < 1250:
    aumento = salario * 0.15
else:
    aumento = salario * 0.10
novo_salario = salario + aumento
print('O salário do funcionário era R$ {:.2f}.'.format(salario))
print('O aumento foi de R$ {:.2f}.'.format(aumento))
print('O novo salário é R$ {:.2f}.'.format(novo_salario))
print('Fim do programa!')
# Faça um algoritmo que leia o salario de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Digite o salário do funcionário: R$'))
aumento = 15
novo_salario = salario + (salario * aumento / 100)
print('O novo salário do funcionário com {}% de aumento é: R${:.2f}'.format(aumento, novo_salario))
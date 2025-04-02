# Tipos primitivos: int, float, bool, str
# Operações aritméticas: +, -, *, /, //, **, %
# Operadores de comparação: ==, !=, >, <, >=, <=
# Operadores lógicos: and, or, not
# Operadores de atribuição: =, +=, -=, *=, /=
# Ordem de precedência: (), **, *, /, //, %, +, -

# Exemplo de uso de variáveis e operações aritméticas
print('Soma de dois números')
n1 = int (input('Digite um número: '))
n2 = int (input('Digite outro número: '))
soma = n1 + n2
print('A soma vale: ', soma,'\n')
print('=' * 20)

# Exemplo de operações aritméticas resto da divisão
print('Resto da divisão')
n1 = int (input('Digite um número: '))
n2 = int (input('Digite outro número: '))
resto = n1 % n2
print('O resto da divisão entre {} e {} é: {}\n'.format(n1, n2, resto))

# Exemplo potencia
print('Potenciação')
n1 = int (input('Digite um número: '))
n2 = int (input('Digite outro número: '))
potencia = n1 ** n2
print('A potência entre {} e {} é: {}\n'.format(n1, n2, potencia))

# Exemplo extrair a parte inteira de uma divisão
print('Valor inteiro da divisão')
n1 = float (input('Digite um número: '))
n2 = float (input('Digite outro número: '))
divisao = n1 // n2
print('A divisão entre {} e {} é: {}\n'.format(n1, n2, divisao))

var = input('Digite algo: ')
print('O tipo primitivo é: ', type(var))
print('Só tem espaços? ', var.isspace())
print('É um número? ', var.isnumeric())
print('É alfabético? ', var.isalpha())
print('É alfanumérico? ', var.isalnum())
print('Está em maiúsculas? ', var.isupper())
print('Está em minúsculas? ', var.islower())
print('Está capitalizada? ', var.istitle())
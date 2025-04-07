# Escreva um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' e 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite o sexo [M/F]: ')).upper()
    if sexo != 'M' and sexo != 'F':
        print('Sexo inválido! Tente novamente.')
print(f'Sexo {sexo} registrado com sucesso!')
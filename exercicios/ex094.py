# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) A média de idade do grupo.
# C) Uma lista com todas as mulheres.
# D) Uma lista com todas as pessoas com idade acima da média.

pessoas = []
cadastro = {}
soma = 0

while True:
    cadastro['nome'] = str(input('Nome: '))
    while True:
        cadastro['sexo'] = str(input('Sexo: [M/F] ')).upper()
        if cadastro['sexo'] in 'MF':
            break
        print('ERRO! Digite apenas M ou F.')
    cadastro['idade'] = int(input('Idade: '))
    soma += cadastro['idade']
    pessoas.append(cadastro.copy())
    while True:
        continuar = str(input('Deseja continuar? [S/N] ')).upper()
        if continuar in 'SN':
            break
        print('ERRO! Digite apenas S ou N.')
    if continuar == 'N':
        break
print('-=' * 30)
print('Analisando os dados...')
media = soma / len(pessoas)
print(f'A) Ao todo foram {len(pessoas)} pessoas cadastradas.')
print(f'B) A media de idade do grupo é de {media:.2f} anos.')
print('C) As mulheres cadastradas foram: ', end='')
for p in pessoas:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()
print('D) Lista das pessoas com idade acima da média:')
for p in pessoas:
    if p['idade'] > media:
        print(f'Nome: {p["nome"]}; Sexo: {p["sexo"]}; Idade: {p["idade"]}')
print('<< ENCERRADO >>')
# Fim do programa

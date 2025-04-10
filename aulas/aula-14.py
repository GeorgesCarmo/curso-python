# Variáveis compostas: Listas parte II

teste = list()
teste.append('Georges')
teste.append(29)
teste2 = list()
teste2.append(teste[:])
teste[0] = 'João'
teste[1] = 19
teste2.append(teste[:])
print(teste2)
galera = [['João', 19], ['Maria', 22], ['Pedro', 21], ['Ana', 20]]
for pessoa in galera:
    print(f'{pessoa[0]} tem {pessoa[1]} anos.')

dados = list()
for c in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()
print(galera)
maior21 = menor21 = 0
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        maior21 += 1
    else:
        print(f'{p[0]} é menor de idade.')
        menor21 += 1
print(f'Temos {maior21} maiores de idade e {menor21} menores de idade.')

# Dicionários

# Estruturas de dados que armazenam pares de chave-valor
# Dicionários em Python se parecem com objetos do JavaScript
# Dicionários em Python se parecem com mapas do Java


# Criando um dicionário
# Dicionário vazio
dicionario = {}
# Dicionário com valores
dicionario = {'chave1': 'valor1', 'chave2': 'valor2', 'chave3': 'valor3'}
# Dicionário com chaves e valores de diferentes tipos
dicionario = {'chave1': 1, 'chave2': 2.5, 'chave3': True, 'chave4': 'valor4'}
print(dicionario)
# Acessando valores do dicionário
print(dicionario['chave1'])
print(dicionario['chave2'])
print(dicionario['chave3'])
print(dicionario['chave4'])
print(dicionario.values())
print(dicionario.keys())
print(dicionario.items())
print(dicionario.get('chave1'))
print(dicionario.get('chave2'))
print(dicionario.get('chave3'))
print(dicionario.get('chave4'))
# Adicionando valores ao dicionário
dicionario['chave5'] = 'valor5'
print(dicionario.get('chave5'))
# Atualizando valores do dicionário
dicionario['chave5'] = 'valor6'
print(dicionario.get('chave5'))
# Removendo valores do dicionário
del dicionario['chave5']
print(dicionario.get('chave5'))
locadora = list()
filme1 = {
    'titulo': 'Star Wars', 'ano': 1977, 'genero': 'Ficção Científica',
}
filme2 = {
    'titulo': 'Matrix', 'ano': 1999, 'genero': 'Ficção Científica',
}
filme3 = {
    'titulo': 'Vingadores', 'ano': 2012, 'genero': 'Ação',
}
filme4 = {
    'titulo': 'Harry Potter', 'ano': 2001, 'genero': 'Fantasia',
}
filme5 = {
    'titulo': 'Senhor dos Anéis', 'ano': 2001, 'genero': 'Fantasia',
}
locadora.append(filme1)
locadora.append(filme2)
locadora.append(filme3)
locadora.append(filme4)
locadora.append(filme5)
for filme in locadora:
    for k, v in filme.items():
        print(f'{k}: {v}')
    print('-' * 20)    

brasil = []
estado1 = {'estado': 'São Paulo', 'sigla': 'SP'}
estado2 = {'estado': 'Rio de Janeiro', 'sigla': 'RJ'}
estado3 = {'estado': 'Minas Gerais', 'sigla': 'MG'}
brasil.append(estado1)
brasil.append(estado2)
brasil.append(estado3)
print(brasil)
print(brasil[0]['estado'])
print(brasil[1]['sigla'])

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['estado'] = str(input('Estado: '))
    estado['sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy())
print(brasil)
for e in brasil:
    for k, v in e.items():
        print(f'O {k} é {v}')
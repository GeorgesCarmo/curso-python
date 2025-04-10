# Estruturas compostas: Listas

lanches = ['hamburguer', 'suco', 'pizza', 'pudim']
print(lanches)
lanches.append('cookie')  # Adiciona 'cookie' ao final da lista
print(lanches)
lanches.insert(0, 'hot dog')  # Adiciona 'hot dog' na posição 0
print(lanches)
del lanches[3]  # Remove o item na posição 3
print(lanches)
lanches.pop()  # Remove o último item da lista, também aceita um índice
print(lanches)
lanches.remove('suco')  # Remove o primeiro item com o valor 'suco'
print(lanches)
lanches.sort()  # Ordena a lista em ordem alfabética
print(lanches)
lanches.sort(reverse=True)  # Ordena a lista em ordem alfabética inversa
print(lanches)
print(f'Essa lista tem {len(lanches)} lanches')
if 'pizza' in lanches:
    print('Tem pizza, vou comer')
    lanches.remove('pizza')  # Remove o primeiro item com o valor 'pizza'
else:
    print('Não tem pizza')
'''
valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for count in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

print(valores)  

for contador, valor in enumerate(valores):
    print(f'Na posição {contador} encontrei o valor {valor}')
print('Cheguei ao final da lista')
'''
a = [2, 3, 4, 7]
b = a
print(f'A: {a}')
print(f'B: {b}')
b[2] = 8
print(f'A: {a}')
print(f'B: {b}')

print('=-' * 20)
a = [2, 3, 4, 7]
b = a[:] # Faz uma cópia da lista
print(f'A: {a}')
print(f'B: {b}')
b[2] = 8
print(f'A: {a}')
print(f'B: {b}')

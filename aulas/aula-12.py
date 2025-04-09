# Variáveis compostas: Tuplas

# Tuplas são listas imutáveis
# Tuplas são definidas com parênteses
# Tuplas podem conter diferentes tipos de dados
# Tuplas podem ser aninhadas
# Tuplas podem ser indexadas
# Tuplas podem ser fatiadas
# Tuplas podem ser concatenadas
# Tuplas podem ser repetidas
# Tuplas podem ser convertidas em listas
# Tuplas podem ser convertidas em strings
# Tuplas podem ser convertidas em dicionários
# Tuplas podem ser convertidas em conjuntos
# Tuplas podem ser convertidas em arrays
# Tuplas podem ser convertidas em bytes
# Tuplas podem ser convertidas em memória compartilhada

lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
print(lanche)
print(sorted(lanche))
print(lanche[0])
print(lanche[1:3])
print(lanche[-1])
print(lanche[-3:])
print(lanche[:3])
print(lanche[:-1])

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')

print(len(lanche))

lanche = ('hamburguer', 'suco', 'pizza', 'pudim', 'batata frita')
for count in range(0, len(lanche)):
    print(lanche[count])

for posicao, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {posicao}')

a = (2, 3, 4)
b = (5, 6, 7, 2)
c = a + b
d = b + a
print(c)  
print(d)
print(c.count(2))  # Conta quantas vezes o valor 2 aparece na tupla c
print(c.index(2, 1))  # Mostra a posição do valor 2 na tupla c, começando a busca a partir do índice 1
print(c.index(2))  # Mostra a posição do valor 2 na tupla c

# Tupla com valores diferentes
pessoa = ('Lucas', 18, 'M', 1.75)
print(pessoa)
# del pessoa
# print(pessoa)
# Estrutura de repetição while

contador = 1
while contador <= 10:
    print(contador)
    contador += 1

print('=' * 20)

r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Deseja continuar? [S/N] ')).upper()
print('Fim')

print('=' * 20)

# Estrutura de repetição while com break
contador = 1
while contador <= 10:
    print(contador)
    contador += 1
    if contador == 5:
        break
print('=' * 20)
# Estrutura de repetição while com continue
contador = 0
while contador <= 10:
    contador += 1
    if contador == 5:
        continue
    print(contador)

print('=' * 20)
# Estrutura de repetição while com else
contador = 1
while contador <= 10:
    print(contador)
    contador += 1
else:
    print('Contador chegou a 10')
print('=' * 20)

# Aprimore o desafio anterior, mostrando no final:
# A soma de todos os valores digitados.
# A soma dos valores da terceira coluna.
# O maior valor da segunda linha

soma = 0
matriz = [[], [], []]
for i in range(3):
    for j in range(3):
        matriz[i].append(int(input(f'Digite um valor para [{i}, {j}]: ')))
        soma += matriz[i][j]
print('-=' * 30)
for i in range(3):
    for j in range(3):
        print(f'[{matriz[i][j]:^5}]', end=' ')
    print()
print('-=' * 30)
print(f'A soma dos valores é: {soma}')
somaColuna = 0
for i in range(3):
    somaColuna += matriz[i][2]
print(f'A soma dos valores da terceira coluna é: {somaColuna}')
maior = matriz[1][0]
for i in range(3):
    if matriz[1][i] > maior:
        maior = matriz[1][i]
print(f'O maior valor da segunda linha é: {maior}')
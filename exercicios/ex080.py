# Crie um programa onde o usuário possa digitar 5 valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.

valores = []
for c in range(0, 5):
    num = int(input(f'Digite o {c + 1} número: '))
    if c == 0 or num > valores[-1]:
        valores.append(num)
        print('Valor adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(valores):
            if num <= valores[pos]:
                valores.insert(pos, num)
                print(f'Valor adicionado na posição {pos} da lista...')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados foram: {valores}')
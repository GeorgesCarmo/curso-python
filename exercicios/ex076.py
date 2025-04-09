# Crie um programa que tenha uma tupla unica com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

print('=-' * 30)
print(f'{"LISTAGEM DE PREÇOS":^60}')
print('=-' * 30)
produtos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20,
            'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
for i in range(0, len(produtos), 2):
    print(f'{produtos[i]:.<50} R${produtos[i + 1]:>7.2f}')
print('=-' * 30)
print(f'{"FIM DO PROGRAMA":^60}')
print('=-' * 30)
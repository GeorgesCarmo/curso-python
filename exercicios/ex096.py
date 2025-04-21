# Faça um programa que tenha uma função chamada área, que receba as dimensões de um terreno retangular
# (largura e comprimento) e mostre a área do terreno.
# A fórmula para calcular a área de um retângulo é: área = largura * comprimento
def area(largura, comprimento):
    a = largura * comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {a}m².')
    return a


# Programa principal
print('Controle de Terrenos')
print('-' * 30)
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
area(largura, comprimento)

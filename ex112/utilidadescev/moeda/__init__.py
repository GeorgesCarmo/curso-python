def aumentar(n1 = 0, n2 = 0, format = False):
    res = n1 + (n1 * n2 / 100)
    return res if format is False else moeda(res)
    
def diminuir(n1 = 0, n2 = 0, format = False):
    res = n1 - (n1 * n2 / 100)
    return res if format is False else moeda(res)

def dobro(n = 0, format = False):
    res = n * 2
    return res if format is False else moeda(res)

def metade(n = 0, format = False):
    res = n / 2
    return res if format is False else moeda(res)

def moeda(n = 0, moeda = 'R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')

def resumo(n = 0, aum = 10, red = 5):
    print('-' * 35)
    print('RESUMO DO VALOR'.center(35))
    print('-' * 35)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'{aum}% de aumento: \t{aumentar(n, aum, True)}')
    print(f'{red}% de redução: \t\t{diminuir(n, red, True)}')
    print('-' * 35)

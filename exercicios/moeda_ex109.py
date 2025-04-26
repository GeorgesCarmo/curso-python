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
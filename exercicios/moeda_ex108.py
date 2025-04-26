def aumentar(n1 = 0, n2 = 0):
    return n1 + (n1 * n2 / 100)
    
def diminuir(n1 = 0, n2 = 0):
    return n1 - (n1 * n2 / 100)

def dobro(n = 0):
    return n * 2
def metade(n = 0):
    return n / 2

def moeda(n = 0, moeda = 'R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')
def fatorial(n):
    """
    Calcula o fatorial de um número inteiro n.
    :param n: número inteiro
    :return: fatorial de n
    """
    if n < 0:
        raise ValueError("O fatorial não está definido para números negativos.")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)
    
def dobro(n):
    return n * 2

def triplo(n):
    return n * 3

def quadrado(n):
    return n * n
    
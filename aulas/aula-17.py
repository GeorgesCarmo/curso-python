'''
    Tópicos da aula: Interactive Help, DocStrings, Argumentos opcionais, Escopo de variáveis, Retorno de funções.
'''

#help(print)  # Ajuda para a função print
#help(len)  # Ajuda para a função len
#help(str)  # Ajuda para a função str
#help(int)  # Ajuda para a função int
#help(float)  # Ajuda para a função float
#help(list)  # Ajuda para a função list

# Exemplo de DocString
def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')

#help(contador)  # Ajuda para a função contador

def somar(a, b, c=0):
    s = a + b + c
    print(f'A soma é {s}')

somar(2, 3)  # Chamada da função somar com dois argumentos
somar(2, 3, 4)  # Chamada da função somar com três argumentos

def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

n = int(input('Digite um número para calcular o fatorial: '))
print(f'O fatorial de {n} é {fatorial(n)}')

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados foram {f1}, {f2} e {f3}')

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False
    
num = int(input('Digite um número: '))
if par(num):
    print(f'O número {num} é par')
else:
    print(f'O número {num} é ímpar')    
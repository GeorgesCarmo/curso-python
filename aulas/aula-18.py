# Estudando modulos e pacotes

# Modulo: um arquivo python que contém funções, classes e variáveis
# Pacote: um diretório que contém um ou mais módulos e um arquivo __init__.py
# O arquivo __init__.py é necessário para que o Python reconheça o diretório como um pacote
# O arquivo __init__.py pode estar vazio ou conter código de inicialização do pacote
# O arquivo __init__.py pode conter importações de outros módulos do pacote
# O arquivo __init__.py pode conter variáveis e funções que serão importadas quando o pacote for importado
# O arquivo __init__.py pode conter a definição de classes que serão importadas quando o pacote for importado

#import funcoes_uteis as uteis
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from uteis import numeros
'''
num = int(input("Digite um número inteiro: "))
fat=uteis.fatorial(num)
print(f"O fatorial de {num} é {fat}.")
print(f"O dobro de {num} é {uteis.dobro(num)}.")
print(f"O triplo de {num} é {uteis.triplo(num)}.")
print(f"O quadrado de {num} é {uteis.quadrado(num)}.")
'''


print('~' * 20)
num = int(input("Digite um número inteiro: "))
fat=numeros.fatorial(num)
print(f"O fatorial de {num} é {fat}.")
print(f"O dobro de {num} é {numeros.dobro(num)}.")
print(f"O triplo de {num} é {numeros.triplo(num)}.")
print(f"O quadrado de {num} é {numeros.quadrado(num)}.")

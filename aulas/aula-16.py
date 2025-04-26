# Funções
# Funções são pequenos programas que realizam tarefas específicas.
# Elas podem ser usadas diversas vezes em um programa.
# Funções podem receber parâmetros e retornar valores.
# Funções são definidas com a palavra-chave def.
# Funções podem ser aninhadas, ou seja, uma função pode chamar outra função.
# Funções podem ser passadas como parâmetros para outras funções.

def soma(a, b):
    resultado = a + b
    print(f'A soma de a + b é {resultado}' )


soma(10, 20)    
soma(a=10, b=20)

def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


valores = [1, 2, 3, 4, 5]
dobra(valores)
print(valores)


def soma2(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')

soma2(5, 2)
soma2(2, 9, 4)
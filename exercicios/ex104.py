# Crie um programa que tenha a função leiaInt() que vai funcionar de forma semelhante à função input() do Python, 
# só que fazendo a validação para aceitar apenas um valor numérico.

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor, digite um número inteiro!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mUsuário preferiu parar o programa!\033[m')
            return 0
        else:
            return n


n = leiaInt('Digite um número: ')
print(f'Voce digitou o número {n}')
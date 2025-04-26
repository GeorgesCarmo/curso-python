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
        
def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg).replace(',', '.'))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor, digite um número real!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mUsuário preferiu parar o programa!\033[m')
            return 0
        else:
            return n
# Tratamendo de Erros e Exceções

# Erros são problemas que ocorrem durante a execução de um programa, enquanto exceções são eventos que interrompem o fluxo normal do programa.
# Exceções são uma forma de lidar com erros de maneira controlada, permitindo que o programa continue a execução ou trate o erro de forma adequada.

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que vocês digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu parar o programa.')
except Exception as erro:
    print(f'Erro desconhecido. Erro: {erro.__cause__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre!')
    
# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

numero = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
          'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True: 
    try:
        num = int(input('Digite um número entre 0 e 20: '))
        if 0 <= num <= 20:
            break
        else:
            print('Número fora do intervalo. Tente novamente.')
    except ValueError:
        print('Entrada inválida. Tente novamente.')
print(f'Você digitou o número {numero[num]}')
carro = int(input('Quantos ano tem seu carro? '))
if carro <= 3:
    print('Seu carro é novo!')
else:
    print('Seu carro é velho!')

print('Carro novo' if carro <= 3 else 'Carro velho')

print('-' * 50)

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print('A média é: {:.1f}'.format(media))
if media >= 7:
    print('Aprovado!')
elif media >= 5:
    print('Recuperação!')
else:
    print('Reprovado!')
# Faça um programa que leia duas notas de um aluno e calcule sua media, mostrando uma mensagem no final de acordo com a media atingida:
# - Media abaixo de 5.0: REPROVADO
# - Media entre 5.0 e 6.9: RECUPERAÇÃO
# - Media 7.0 ou superior: APROVADO
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print('A média entre {} e {} é: {:.2f}'.format(n1, n2, media))
if media < 5:
    print('REPROVADO')
elif media >= 5 and media < 7:
    print('RECUPERAÇÃO')
elif media >= 7:
    print('APROVADO')
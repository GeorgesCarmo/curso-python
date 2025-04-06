# A confederação nacional de natacao precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JUNIOR
# - Até 25 anos: SENIOR
# - Acima: MASTER
from datetime import date
ano = int(input('Qual é o seu ano de nascimento? '))
idade = date.today().year - ano
print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, date.today().year))
if idade <= 9:
    print('Voce é da categoria MIRIM.')
elif idade <= 14:
    print('Voce é da categoria INFANTIL.')
elif idade <= 19:
    print('Voce é da categoria JUNIOR.')
elif idade <= 25:
    print('Voce é da categoria SENIOR.')
else:
    print('Voce é da categoria MASTER.')
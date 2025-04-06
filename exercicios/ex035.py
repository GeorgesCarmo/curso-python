# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a idade dele, se ele ainda vai se alistar ao serviço militar,
# se é a hora de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deve mostrar o tempo que falta ou que passou do prazo.
from datetime import date
ano = int(input('Qual é o seu ano de nascimento? '))
idade = date.today().year - ano
print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, date.today().year))
if idade < 18:
    print('Ainda faltam {} anos para o alistamento.'.format(18 - idade))
    print('Seu alistamento sera em {}.'.format(date.today().year + (18 - idade)))
elif idade == 18:
    print('Voce deve se alistar IMEDIATAMENTE!')
else:
    print('Voce ja deveria ter se alistado ha {} anos.'.format(idade - 18))
    print('Seu alistamento foi em {}.'.format(date.today().year - (idade - 18)))
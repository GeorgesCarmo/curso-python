# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
# Considere que a aposentadoria será com 35 anos de contribuição.

from datetime import date
dados = {}
dados['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de Nascimento: '))
dados['idade'] = date.today().year - nascimento
dados['ctps'] = int(input('Carteira de Trabalho (0 se nenhuma): '))
if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano de Contratação: '))
    dados['salario'] = float(input('Salário: '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35) - date.today().year)
print('-=' * 30)
for k, v in dados.items():
    print(f' - {k} tem o valor {v}')
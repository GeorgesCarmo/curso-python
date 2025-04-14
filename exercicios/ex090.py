# Faça um programa que leia o nome e a média de um aluno, guardando também a situação (Aprovado, Reprovado ou Recuperação) em um dicionário. 
# No final, mostre o conteúdo da estrutura na tela.

alunos = dict()
alunos['nome'] = str(input('Nome: '))
alunos['media'] = float(input('Média: '))
if alunos['media'] >= 7:
    alunos['situacao'] = 'Aprovado'
elif alunos['media'] >= 5:
    alunos['situacao'] = 'Recuperação'
else:
    alunos['situacao'] = 'Reprovado'
for k, v in alunos.items():
    print(f'{k} = {v}')
    
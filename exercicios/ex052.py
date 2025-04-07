# Desenvolva um programa que leia nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# A média de idade do grupo
# Qual é o nome do homem mais velho
# Quantas mulheres têm menos de 20 anos


soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_homem_mais_velho = ''
cont_mulheres_menor_20 = 0
for c in range(1, 5):
    nome = str(input('Qual o nome da {}ª pessoa? '.format(c))).strip()
    idade = int(input('Qual a idade da {}ª pessoa? '.format(c)))
    sexo = str(input('Qual o sexo da {}ª pessoa? [M/F] '.format(c))).strip().upper()
    soma_idade += idade
    if c == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_homem_mais_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_homem_mais_velho = nome
    if sexo in 'Ff' and idade < 20:
        cont_mulheres_menor_20 += 1

media_idade = soma_idade / 4
print('A média de idade do grupo é de {} anos'.format(media_idade))    
print('O homem mais velho tem {} anos e se chama {}'.format(maior_idade_homem, nome_homem_mais_velho))
print('A quantidade de mulheres com menos de 20 anos é de {}'.format(cont_mulheres_menor_20))

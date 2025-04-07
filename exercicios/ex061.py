# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

print("=" * 20)
print("MÉDIA, MAIOR E MENOR VALORES")
print("=" * 20)
soma = cont = maior = menor = 0
while True:
    n = int(input("Digite um número (ou 0 para parar): "))
    if n == 0:
        break
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    continuar = str(input("Deseja continuar? [S/N] ")).upper()
    if continuar == 'N':
        break
if cont > 0:
    media = soma / cont
    print(f"A média dos {cont} números é {media:.2f}.")
    print(f"O maior número digitado foi {maior}.")
    print(f"O menor número digitado foi {menor}.")
else:
    print("Nenhum número foi digitado.")
print("Programa encerrado.")

print("=" * 20)

resposta = 'S'
soma = quant = media = maior = menor = 0
while resposta in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
media = soma / quant
print(f'A soma dos {quant} números é {soma}.')
print(f'A média dos números é {media:.2f}.')
print(f'O maior número é {maior} e o menor é {menor}.')
print("Programa encerrado.")    
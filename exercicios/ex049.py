# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

# Exemplo de palíndromo: "A mala nada na lama"

frase = str(input("Digite uma frase: ")).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = junto[::-1]
print(f"O inverso de {junto} é {inverso}")
if inverso == junto:
    print("Temos um palíndromo!")
else:
    print("A frase digitada não é um palíndromo!")
print("FIM")
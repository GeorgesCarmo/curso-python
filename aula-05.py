# Analisando frases
frase = 'Curso em Video Python'
# Analisando a frase
print(frase)
print(frase[0])  # Primeira letra
print(frase[0:5])  # Primeira letra até a quinta letra
print(frase[:5])  # Primeira letra até a quinta letra
print(frase[15:])  # De 15 em diante
print(frase[9::3])  # De 9 em diante, pulando de 3 em 3
print(len(frase))  # Tamanho da string
print(frase.count('o'))  # Contar quantas letras 'o' tem na frase
print(frase.count('o', 0, 13))  # Contar quantas letras 'o' tem na frase entre o índice 0 e 13
print(frase.find('deo'))  # Encontrar a posição da letra 'deo'
print(frase.find('Android'))  # Encontrar a posição da letra 'Android'
print('Curso' in frase)  # Verifica se 'Curso' está na frase
print(frase.replace('Python', 'Android'))  # Troca 'Python' por 'Android'
print(frase.upper())  # Coloca tudo em maiúsculo
print(frase.lower())  # Coloca tudo em minúsculo
print(frase.capitalize())  # Coloca a primeira letra em maiúsculo
print(frase.title())  # Coloca a primeira letra de cada palavra em maiúsculo
print(frase.strip())  # Remove os espaços no início e no fim
print(frase.rstrip())  # Remove os espaços no fim
print(frase.lstrip())  # Remove os espaços no início
print(frase.split())  # Divide a frase em palavras
print(frase.split()[0])  # Pega a primeira palavra
print('-'.join(frase))  # Coloca um '-' entre cada letra
div = frase.split()
print(div[0][1])  # Pega a segunda letra da primeira palavra
# Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, 
# sabendo que cada litro de tinta pinta uma área de 2m².
largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))
area = largura * altura
tinta = area / 2
print('A área da parede é {:.2f} m² e a quantidade de tinta necessária para pintá-la é {:.2f} litros'.format(area, tinta))

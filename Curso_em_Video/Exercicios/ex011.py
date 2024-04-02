# Faça um programa que leia a largura e a altura de uma parete em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 m².
a = float(input('Digite a altura da parede: '))
l = float(input('Digite a largura da parede: '))
print('A parede tem {} metros de altura e {} metros de largura, ou seja, uma área de {} metros². \nA quantidade de tinta necessária para pintá-la é {} litros.'.format(a, l, a*l, (a*l)/2))
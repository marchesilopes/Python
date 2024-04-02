# Faça um programa que leia o comprimentio do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule
# e mostre o comprimento da hipotenusa.
import math

co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
print('O comprimento da hipotenusa é {}'.format(math.sqrt((math.pow(co,2)+math.pow(ca,2)))))

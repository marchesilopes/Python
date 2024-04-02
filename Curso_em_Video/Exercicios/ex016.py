# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
import math
n = float(input('Digite um número real: '))
print('Você digitou o número {}, a parte inteira desse número é {}.'.format(n, math.trunc(n)))
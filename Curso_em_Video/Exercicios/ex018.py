# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangênte desse ângulo.
import math

a = float(input('Digite o valor do ângulo: '))
print('Você digitou o valor de {} graus. O seno deste ângulo é {}, o cosseno é {} e a tangente é {}'.format(a, math.sin(a), math.cos(a), math.tan(a)))
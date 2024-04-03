# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random

n = random.randrange(0, 5, 1)

d = int(input('Qual foi o número escolhido pelo computador? '))

if n == d:
    print('Parabéns, o computador escolheu o número {}'.format(n))
else:
    print('Você errou, o computador escolheu o número {}'.format(n))
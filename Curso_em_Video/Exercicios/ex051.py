# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa
# progressão.
a = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))

for c in range(1, 11):
    print('O valor do {}º termo da PA é: {}'.format(c, a+(c-1)*r))
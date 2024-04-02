# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

n = str(input('Digite um número: '))

print('Unidade: {}'.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('Centena: {}'.format(n[1]))
print('Milhar: {}'.format(n[0]))
# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
ano = int(input('Digite um ano: '))

if (ano % 400) == 0:
    print('O ano é bissexto!')
else:
    if (ano % 4) == 0 and (ano % 100) != 0:
        print('O ano é bissexto!')
    else:
        print('O ano NÃO é bissexto!')

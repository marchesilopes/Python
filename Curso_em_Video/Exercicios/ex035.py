# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo
r1 = float(input('Digite o comprimento da reta 1: '))
r2 = float(input('Digite o comprimento da reta 2: '))
r3 = float(input('Digite o comprimento da reta 3: '))

if r1 < (r2 + r3):
    if (r1 + r2) > r3:
        print('As retas formam um triângulo')
    else:
        print('As retas NÃO formam um triângulo')
else:
    print('As retas NÃO formam um triângulo')
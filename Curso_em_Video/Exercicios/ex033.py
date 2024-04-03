# Fala um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

if n1 > n2:
    if n1 > n3:
        print('O maior número é {}'.format(n1))
    else:
        print('O maior número é {}'.format(n3))
else:
    if n2 > n3:
        print('O maior número é {}'.format(n2))
    else:
        print('O maior número é {}'.format(n3))
print('== FIM ==')
# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no
# no intervalo de 1 até 500.
s = 0
for c in range(3, 500, 3):
    print(c)
    n = c
    s += n
print('A soma de todos os números ímpares que são múltiplos de 3 e se encontram no intervalo é {}.'.format(s))
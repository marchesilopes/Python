# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero: todos os lados iguais
# Isósceles: dois lados iguais
# Escaleno: todos os lados diferentes

r1 = float(input('Digite o comprimento da reta 1: '))
r2 = float(input('Digite o comprimento da reta 2: '))
r3 = float(input('Digite o comprimento da reta 3: '))

if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):    
    if r1 == r2 == r3:
        print('As retas forma um triângulo Equilátero.')
    elif (r1 == r2) or (r1 == r3) or (r2 == r3):
        print('As retas forma um triângulo Isósceles.')
    else:
        print('As retas forma um triângulo Escaleno.')
else:
    print('As retas NÃO formam um triângulo')

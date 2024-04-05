#i = int(input('Digite o início: '))
#f = int(input('Digite o fim: '))
#p = int(input('Digite o passo: '))
#for c in range(i, f+1, p):
#    print(c)
#print('FIM')

s = 0
for c in range (0, 4):
    n = int(input('Digite um número: '))
    s += n
print('O somatório de todos os valores foi {}.'.format(s))
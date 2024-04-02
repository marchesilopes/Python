# OPERAÇÕES ARITMÉTICAS
# + = Adição
# - = Subtração
# * = Multiplicação
# / = Divisão
# ** = Potência
# // = Divisão inteira
# % = Resto da divisão

#print(5+2)
#print(5-2)
#print(5*2)
#print(5/2)
#print(5**2)
#print(5//2)
#print(5%2)

## ORDEM DE PRECEDÊNCIA
# 1 - ()
# 2 - **
# 3 - * / // %
# 4 - + - 

#print(5 + 3 * 2)
#print(3 * 5 + 4 ** 2)
#print(3 * (5 + 4) ** 2)

#nome = input('Qual é o o seu nome? ')
#print('Prazer em te conhecer {:=^20}!'.format(nome))

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma vale {}, \n o produto é {} e a \n divisão é {:.3f}'.format(s, m, d), end=' >>> ')
print('Divisão inteira {} e potência {}'.format(di, e))
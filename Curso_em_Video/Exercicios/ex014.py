# Escreva um programa que converta uma temperatura digitada em ºC para ºF.
temp = float(input('Digite a temperatura em ºC: '))
print('A temperatura de {}ºC é equivalente a temperatura de {}ºF.'.format(temp, (temp*1.8)+32))
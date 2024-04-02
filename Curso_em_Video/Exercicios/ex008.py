# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
n = float(input('Digite o valor em metros: '))
print('Você digitou {} metros, este valor corresponde à medida de {} centímetros ou então a {} milímetros.'. format(n, n*100, n *1000))
# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.
v = float(input('Digite a velocidade do carro: '))

if v > 80:
    print('O carro ultrapassou 80 km/h. A velocidade foi de {} km/h e o valor da multa de {} reais.'. format(v, (v-80)*7))
else:
    print('O carro está dentro do limite de velocidade.')
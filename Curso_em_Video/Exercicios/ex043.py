# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule o seu IMC e mostre seu status, de acordo com a
# tabela abaixo:
# Abaixo de 18.5: Abaixo do Peso
# Entre 18.5 e 25: Peso ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade Mórbida
a = float(input('Qual sua altura? '))
p = float(input('Qual seu peso? '))
imc = p/(a**2)

if imc < 18.5:
    print('Seu IMC é de {} kg/m², você está ABAIXO DO PESO.'.format(imc))
elif imc < 25:
    print('Seu IMC é de {} kg/m², você está no PESO IDEAL.'.format(imc))
elif imc < 30:
    print('Seu IMC é de {} kg/m², você está com SOBREPESO.'.format(imc))
elif imc < 40:
    print('Seu IMC é de {} kg/m², você está com OBESIDADE.'.format(imc))
else:
    print('Seu IMC é de {} kg/m², você está com OBESIDADE MÓRBIDA.'.format(imc))
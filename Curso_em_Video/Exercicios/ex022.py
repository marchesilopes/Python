# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minúsculas
# Quantas letras ao todo (sem considerar espaços)
# Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: ')).strip()

print('Analisando seu nome...')
print('O nome com todas as letras maiúsculas é: {}'.format(nome.upper()))
print('O nome com todas as letras minúsculas é: {}'.format(nome.lower()))
print('O nome possui {} letras, sem considerar os espaços.'.format(len(nome) - nome.count(' ')))
print('O primeiro nome possui {} letras.'.format(len(nome.split()[0])))
# Crie um programa que leia uma frase qualquer e diga se ela é palíndromo, desconsiderando os espaços e acentos.
# APOS A SOPA
# A SACADA DA CASA
# A TORRE DA DERROTA
# O LOBO AMA O BOLO
# ANOTARAM A DATA DA MARATONA

frase = str(input('Digite uma frase: ')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

print('Você digitou a frase {}'.format(junto))

for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]

print('O inverso de {} é {}.'.format(junto, inverso))

if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo')
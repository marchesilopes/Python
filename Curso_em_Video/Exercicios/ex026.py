# Faça um programa que leia uma frase no teclado e mostre:
# Quantas vezes aparece a letra "A"
# Em que posição ela aparece a primeira vez.
# Em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).upper().strip()

print('Analisando a frase...')
print('A letra "a" aparece {} vezes na frase'.format(frase.count('A')))
print('A letra "a" aparece pela primeira vez na posição {}.'.format(frase.find('A')))
print('A letra "a" aparece pela última vez na posição {}.'.format())
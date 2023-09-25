'''Faça um programa que leia uma frase pelo teclado e mostre:
1 - Quantas vezes aparece a letra "A"
2 - Em que posição ele aparece a primeira vez
3 - emque posição ela aparece a última vez'''

frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))

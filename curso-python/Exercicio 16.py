#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira. EX: digite um número: 6.127 | O número 6.127 tem a parte inteira 6.

from math import floor
num = float(input('Digite um número: '))
print('O número {} tem a parte inteira {}'.format(num, (floor(num))))

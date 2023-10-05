'''Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:

O primeiro valor é maior
o segundo valor é maior
Não existe valor maior, os dois são iguais'''

a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
if b < a:
    print('O primeiro valor é maior')
elif a < b:
    print('O segundo valor é maior')
else:
    print('Não existe valor maior, os dois são iguais')

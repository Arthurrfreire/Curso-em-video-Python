'''Faça um programa que leia um número inteiro e diga se ele é ou não um número primo
'''
numero = int(input('Digite um número inteiro: '))

if numero <= 1:
    primo = False
elif numero == 2:
    primo = True
else:
    primo = True
    for i in range(3, int(numero**0.5) + 1, 2):
        if numero % i == 0:
            primo = False
            break

if primo:
    print('ESSE NÚMERO É PRIMO')
else:
    print('ESSE NÚMERO NÃO É PRIMO')

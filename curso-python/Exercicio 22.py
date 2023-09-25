'''Crie um programa que leia o nome completo de uma pessoa e mostre
1 - o nome com todas as letras maiúsculas
2 - O nome com todas minúsculas
3 - Quantas letras ao todo (sem considerar espaços)
4 - Quantas letras tem o primeiro nome'''

nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

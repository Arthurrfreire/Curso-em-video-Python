'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o'''

soma_pares = 0
for c in range(6):
    numero = int(input('Digite um número inteiro: '))
    if numero % 2 == 0:
        soma_pares += numero
print('A soma de todos os números pares foi {}'.format(soma_pares))

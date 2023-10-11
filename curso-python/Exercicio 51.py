'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão'''

termo = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = termo + (10 - 1) * razão
for c in range(termo, décimo + razão, razão):
    print('{} '.format(c), end=' -> ')
print('ACABOU')

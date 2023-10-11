'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão'''

termo = int(input('Digite o termo da PA: '))
razão = int(input('Digite a razão da PA: '))
for c in range(10):
    termo_n = termo + c * razão
    print('O {}º termo da PA é: {}'.format(c + 1, termo_n))
    
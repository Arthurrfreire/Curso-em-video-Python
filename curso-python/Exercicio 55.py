'''Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos
'''

maiores = float('-inf')
menores = float('inf')

for c in range(5):
    peso = float(input('Digite o peso da {}ª (kg): '.format(c+1)))

    if peso > maiores:
        maiores = peso
    if peso < menores:
        menores = peso

print('O maior peso lido foi: {:.2f}'.format(maiores))
print('O menor peso lido foi: {:.2f}'.format(menores))

'''Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atigiram a maioridade e quantas já são maiores
considerando a maioridade 21 anos'''

from datetime import date
atual = date.today().year
menores = 0
maiores = 0

for c in range(1, 8):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    idade = atual - ano
    
    if idade < 21:
        menores += 1
    else:
        maiores += 1

print('Total de pessoas menores de idade: {}'.format(menores))
print('Total de pessoas maiores de idade: {}'.format(maiores))

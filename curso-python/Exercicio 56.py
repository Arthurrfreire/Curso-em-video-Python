'''Desenvolva um programa que leia o nome. idade e sexo de 4 pessoas. No final do programa, mostre:
- A média de idade do grupo
- Qual é o nome do homem mais velho
- Quantas mulheres têm menos de 20 anos.
'''

soma_idade = 0
idade_homem_mais_velho = 0
nome_homem_mais_velho = ''
mulheres_menos_20_anos = 0

for c in range(4):
    print('Pessoa: {}'.format(c+1))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M/F): ').upper()).strip()

    soma_idade += idade

    if sexo == 'M' and idade > idade_homem_mais_velho:
        idade_homem_mais_velho = idade
        nome_homem_mais_velho = nome

    if sexo == 'F' and idade < 20:
        mulheres_menos_20_anos += 1

media_idade = soma_idade / 4

print('\nMédia de idade do grupo: {:.2f} anos'.format(media_idade))

if nome_homem_mais_velho:
    print('O homem mais velho é {} com {} anos.'.format(nome_homem_mais_velho, idade_homem_mais_velho))
else:
    print('Não foi informado nenhum homem.')

print('{} mulher(es) têm menos de 20 anos.'.format(mulheres_menos_20_anos))

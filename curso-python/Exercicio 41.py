'''A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 20 anos: SÊNIOR
- Acima: Master'''

from datetime import date
atual = date.today().year
ano = int(input('Digite o ano de nascimento do atleta: '))
idade = atual - ano
if idade <= 9:
    print('Com a idade de {} anos o atleta é da categoria MIRIM'.format(idade))
elif 9 < idade <= 14:
    print('Com a idade de {} anos o atleta é da categoria INFANTIL'.format(idade))
elif 14 < idade <= 19:
    print('Com a idade de {} anos o atleta é da categoria JUNIOR'.format(idade))
elif 19 < idade <= 20:
    print('Com a idade de {} anos o atleta é da categoria SÊNIOR'.format(idade))
else:
    print('Com a idade de {} anos o atleta é da categoria MASTER'.format(idade))

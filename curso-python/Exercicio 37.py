'''Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher que será a base de conversão: 

1 para binário
2 para octal
3 para hexadecimal'''

num = int(input('Digite um número: '))
base = int(input('Em qual base será convertido:\n[ 1 ] para binário\n[ 2 ] para octal\n[ 3 ] para hexadecimal\nSua opção: '))
if base == 1:
    b = bin(num)
    print('O número {} convertido para binário é {}'.format(num, b))
elif base == 2:
    o = oct(num)
    print('O número {} convertido para octal é {}'.format(num, o))
elif base == 3:
    h = hex(num)
    print('O número {} convertido para hexadecimal é {}'.format(num, h))
     
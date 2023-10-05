'''Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher que será a base de conversão: 

1 para binário
2 para octal
3 para hexadecimal'''

num = int(input('Digite um número inteiro: '))
print('''Em qual base será convertido:
[ 1 ] para binário
[ 2 ] para octal
[ 3 ] para hexadecimal''')
opção = int(input('Sua opção: '))             
if opção == 1:
    print('O número {} convertido para binário é {}'.format(num, bin(num) [2:]))
elif opção == 2:
    print('O número {} convertido para octal é {}'.format(num, oct(num) [2:]))
elif opção == 3:
    print('O número {} convertido para hexadecimal é {}'.format(num, hex(num) [2:]))
else:
    print('Opção inválida. Tente novamente')
     
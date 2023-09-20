#Faça um programa que lei um número inteiro e mostre na tela o seu sucessor e seu antecessor

numero = int(input('Digite um número: '))
antecessor = numero - 1
sucessor = numero + 1
print('O antecessor de {} é {} e o sucessor é {} '.format(numero, antecessor, sucessor))

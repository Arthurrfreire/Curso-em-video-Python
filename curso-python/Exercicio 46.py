'''Faça um programa que mostre na tela uma contagem REGRESSIVA para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles'''

from time import sleep
for c in range(10, -1, -1):
    sleep(0.5)
    print(c)
    sleep(0.5)
print('FELIZ ANO NOVO!')

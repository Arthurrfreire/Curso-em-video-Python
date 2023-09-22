#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

import math
oposto = int(input('Digite o Seno: '))
adjacente = int(input('Digite o Cosseno: '))
hipo = math.sqrt(oposto**2 + adjacente**2)
print('O comprimento da hipotenusa é: {:.2f}'.format(hipo))

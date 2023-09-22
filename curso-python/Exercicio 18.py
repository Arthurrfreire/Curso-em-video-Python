#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
angulo_graus = float(input('Digite o valor do ângulo em graus: '))
angulo_radianos = math.radians(angulo_graus)
seno = math.sin(angulo_radianos)
cosseno = math.cos(angulo_radianos)
tangente = math.tan(angulo_radianos)
print('O seno do ângulo é {:.2f}, o cosseno do ângulo é {:.2} e a tangente do ângulo é {:.2f}'.format(seno, cosseno, tangente))

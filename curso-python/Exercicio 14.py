#Escreva um programa que converta uma temperatura digitada em ºC e converta em ºF

temp = float(input('Digite a temperatura em celcius: '))
nova = (temp * 9/5) + 32
print('A temperatura {:.2f}ºC em fahrenheit é {:.2f}ºF '.format(temp, nova))

'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:

- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida
'''

peso = float(input('Digite seu peso: (kg) '))
altura = float(input('Digite sua altura: (m) '))
imc = peso / (altura**2)
if imc <= 18.5:
    print('Se você pesa {:.2f}kg e sua altura é de {:.2f}m, seu IMC é {:.1f} kg/m², portanto você estar abaixo do peso!'.format(peso, altura, imc))
elif 18.5 <= imc <= 25:
    print('Se você pesa {:.2f}kg e sua altura é {:.2f}m, seu IMC é {:.1f} kg/m², portanto seu peso é ideal'.format(peso, altura, imc))
elif 25 <= imc <= 30:
    print('Se você pesa {:.2f}kg e sua altura é {:.2f}m, seu IMC é {:.1f} kg/m², portanto você estar com sobrepeso'.format(peso, altura, imc))
elif 30 <= imc <= 40:
    print('Se você pesa {:.2f}kg e sua altura é {:.2f}m, seu IMC é {:.1f} kg/m², portanto você estar obeso'.format(peso, altura, imc))
else:
    print('Se você pesa {:.2f}kg e sua altura é {:.2f}m, seu IMC é {:.1f} kg/m², portanto você estar com obesidade mórbida'.format(peso, altura, imc))

peso = float(input('Digite seu peso (Kg): '))
altura = float(input('Digite sua altura (m): '))
imc = peso / (altura ** 2)
print('Você está com uma massa corporal de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO da média de peso.')
elif imc <= 25:
    print('Você está no peso IDEAL')
elif imc < 30:
    print('Você está com um nível de SOBREPESO.')
elif imc <= 40:
    print('Você está com um nível de OBESIDADE.')
else:
    print('Você está com um nível de OBESIDADE MÓRBIDA.')
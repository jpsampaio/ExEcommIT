cont = soma = 0
while True:
    num = int(input('Digite um número (999 para finalizar) : '))
    if num == 999:
        break
    cont += 1
    soma = soma + num
print(f'{cont} números foram digitados e a soma deles é {soma}')
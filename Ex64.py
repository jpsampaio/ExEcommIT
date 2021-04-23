cont, soma, num = -1, 0, 0
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números, que juntos somam {}'.format(cont, soma))
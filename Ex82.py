l1 = []
l2 = []
l3 = []
r = 's'
while r == 's':
    x = int(input('Digite um número: '))
    if x % 2 == 0 and x != 0:
        l2.append(x)
    elif x % 2 == 1 and x != 0:
        l3.append(x)
    l1.append(x)
    r = str(input('Quer continuar? [S/N] ')).strip()
    while r not in 'sSnN':
        r = str(input('Digite S ou N: '))
print(f'A lista com todos os valores é {l1}')
print(f'A lista com os valores pares é {l2}')
print(f'A lista com os valores impares é {l3}')
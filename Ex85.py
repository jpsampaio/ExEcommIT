numeros = []
for c in range (0,7):
    numeros.append(int(input(f'Digite o {c+1}º valor:')))
numeros.sort()
print('Lista de números pares: ', end=' ')
for n in numeros:
    if n % 2 == 0:
        print(f'{n}', end=' ')
print('')
print('Lista de numeros impares: ', end=' ')
for n in numeros:
    if n % 2 != 0:
        print(f'{n}', end=' ')
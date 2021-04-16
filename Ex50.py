n1 = int(input('N1:'))
n2 = int(input('N2: '))
n3 = int(input('N3: '))
n4 = int(input('N4: '))
n5 = int(input('N5: '))
n6 = int(input('N6: '))

soma = 0
if n1 % 2 == 0:
    soma += n1
if n2 % 2 == 0:
    soma += n2
if n3 % 2 == 0:
    soma += n3
if n4 % 2 == 0:
    soma += n4
if n5 % 2 == 0:
    soma += n5
if n6 % 2 == 0:
    soma += n6
else:
    print('Numero impar')

print('A soma dos números Pares é {}'.format(soma))
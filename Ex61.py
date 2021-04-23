a = int(input('Digite o primeiro termo da P.A: '))
b = int(input('Digite a razão da P.A: '))
c = int(input('Digite a quantidade de termos da P.A: '))
d = a
print('-'*(c*6))
while d != (a+(b*c)):
    print(f'{d} → ', end='')
    d += b
print('FIM')
print('-'*(c*6))
n = int(input('Digite um número entre 0 e 9999: '))
n2 = str(int(10000 + n))
print('{} milhares.'.format(n2[1]))
print('{} centenas. '.format(n2[2]))
print('{} dezenas. '.format(n2[3]))
print('{} unidades.'.format(n2[4]))
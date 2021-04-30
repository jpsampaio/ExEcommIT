def area(lar, comp):
    a = lar * comp
    return a


print(f'{"Controle de Terrenos":^30}')
print('-' * 30)
lar = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))
print(f'A área de um terreno {lar}x{comp} é de {area(lar, comp):.2f}m².')
lista_num = list()

for x in range(5):
    valor = int(input('Digite o valor: '))
    if x == 0:
        lista_num.append(valor)
        print(f'O número foi adicionado na posição {lista_num.index(valor)} da lista! ')
    else:
        for c in range(len(lista_num)):
            if valor <= lista_num[c]:
                lista_num.insert(c , valor)
                break
        if valor > lista_num[c]:
            lista_num.append(valor)
        print(f'O número foi adicionado na posição {lista_num.index(valor)} da lista! ')

print ('\n',lista_num)
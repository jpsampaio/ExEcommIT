l = int(input('Quantas linhas terá a matriz: '))
c = int(input('Quantas colunas terá a matriz: '))
print(f'Será uma matriz [{l}x{c}]')
matriz = []
for i in range(0,l):
    matriz.append(list())
for i in range(0,l):
    for j in range(0,c):
        matriz[i].append(list())
for i in range(0,l):
    for j in range(0,c):
        matriz[i][j].append(input(f'Elemento [{i}x{j}]: '))
print('='*24)
print('-'*8,'Matriz','-'*8)
print('='*24)
for i in range(0,l):
    print(f'|{matriz[i]}|')
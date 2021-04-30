Matriz = [[[], [], []], [[], [], []], [[], [], []]]
spares = scoluna3 = maiorl2 = 0

for l in range(0, 3):
    for c in range(0, 3):
        Matriz[l][c] = (int(input(f'Digite um valor para [{l}, {c}]: ')))
        if Matriz[l][c] % 2 == 0:
            spares += Matriz[l][c]
        if c == 2:
            scoluna3 += Matriz[l][c]
        if l == 1 and c == 0:
            maiorl2 = Matriz[l][c]
        elif l == 1 and Matriz[l][c] > maiorl2:
            maiorl2 = Matriz[l][c]

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{Matriz[l][c]:^10}]', end='')
    print()

print('=-='*15)
print(f'A soma dos números pares é {spares}')
print(f'A soma dos valores da terceira coluna é {scoluna3}')
print(f'O maior valor da segunda linha é {maiorl2}')
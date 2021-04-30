lista = []
while True:
    n = int(input('Digite um número inteiro: '))
    if n in lista:
        print('ESSE NÚMERO JÁ CONSTA NA LISTA.')
        lista.remove(n)

    lista += [n]

    flag = str(input('Continuar? (S/N): ')).strip().lower()[0]
    if flag == 'n':
        print(f'\nOs números digitados foram {sorted(lista)}')
        break
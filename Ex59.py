n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
op = 0
sair = 5
while op != 5:
    print('-='*15)
    op = int(input('Escolha a sua operação:'
                   '\n[1] Soma.'
                   '\n[2] Multiplicar. '
                   '\n[3] Maior. '
                   '\n[4] Novos números. '
                   '\n[5] Sair do programa.'
                   '\nEscolha a sua opção: '))
    print(f'\n>>>> Qual é a sua opção? {op}', end='')
    if op == 1:
        print(f'\n{n1} + {n2} = {n1+n2}.')
    elif op == 2:
        print(f'\n{n1} x {n2} = {n1*n2}.')
    elif op ==3:
        if n1 > n2:
            print(f'\n {n1} > {n2}')
        elif n1 == n2:
            print('\nOs números são iguais.')
        else:
            print(f'\n{n2} > {n1}')
    elif op ==4:
        print('\nEscolha novos números.  ')
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
        # printa isso e volta pro começo  do while
    elif op == 5:
        print('\nFIM DO PROGRAMA')
    else:
        print('\nOperação inválidada, tente novamente.')
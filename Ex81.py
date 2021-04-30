valores = []
c = f = 0
while True:
    while True:
        n = input('Digite um valor: ')
        if n.isdigit() == True:
 # verifica se o valor é um número.
            n = int(n)
            valores.append(n)
            c += 1
            if n == 5:
                f += 1
 # conta a quantidade de números 5 da lista (caso tenha).
            break
        else:
            print('Valor inválido. ', end='')
    while True:
        resp = str(input('Deseja continuar?[S/N]: ')).strip().upper()
        if resp == 'S' or resp == 'N':
            break
        else:
            print('Resposta inválida. ', end='')
    if resp == 'N':
        break
    print('-' * 30)
valores.sort(reverse=True)
print('-=' * 30)
print(f'Números digitados: {c}')
print(f'Lista decrescente dos valores digitados: {valores}')
if f >= 1:
    print(f'Há {f} número(s) 5 na lista.')
else:
    print('Não há nenhum número 5 na lista.')
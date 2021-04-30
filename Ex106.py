def tit(msg, c):

    n = len(msg)

    if c == 3:
        i = "\033[7:36m"

    if c == 1:
        i = "\033[7:31m"

    if c == 2:
        i = "\033[7:32m"

    if c == 0:
        i = "\033[7:30m"
    f = "\033[m"
    print(f'{i}=' * (n + 4))
    print(f'{i}  {msg}  ')
    print(f'{i}=' * (n + 4))
    print(f)


def biblio():
    while True:
        tit('SISTEMA DE AJUDA PyHELP', 2)
        func = str(input('Função ou Biblioteca >> '))
        tit(f'Acessando o manual de "{func}"', 3)
        if func.upper() in 'FIM':
            tit('ATÉ LOGO!', 1)
            break
        print(f"\033[7:30m"), help(func)
        print("\033[m")


biblio()
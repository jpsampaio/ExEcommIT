def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('Valor inválido, Digite um número inteiro')
        else:
            print(f'O valor inteiro é {num}')
            break

leiaInt('Digite um valor inteiro: ')
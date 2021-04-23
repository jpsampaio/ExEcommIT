from random import randint

v = 0
while True:
    op = str(input('Par ou Ímpar? ')).strip().upper()[0]
    mão = int(input('Quantos dedos [1 - 5]: '))
    pc = randint(1, 5)
    print(f'O PC jogou {pc}.')
    ganha = ''
    if ((mão + pc) % 2) == 0:
        ganha = 'P'
    else:
        ganha = 'I'
    if op == ganha:
        v += 1
        print('OP Ganha.')
    else:
        print('PC Ganha')
        break
print(f'Fim do programa. Você ganhou {v} vezes antes de perder.')
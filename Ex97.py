def dlin(tlin, tam):
    print('=' * tam if tlin == 2 else '-' * tam)

def escreva(texto, tlin, qlin):
    comp = len(texto)
    if qlin == 2:
        dlin(tlin, comp)
    print(f'{texto:<{comp}}')
    dlin(tlin, comp)

escreva('Curso em Vídeo', 2, 2)
escreva('Curso de Python 3 - Mundo 3', 1, 2)
escreva('Desafio #097', 1, 1)

msg = str(input('\nDigite uma frase ou uma palavra: ')).strip().title()
dlin(1, 25)
tipo_linha = int(input('escolha [1] para linha simples "-" ou [2] para linha dupla "=": '))
dlin(1, 25)
qnt_linha = int(input('Escolha [1] para apenas a linha inferior ou [2] para linha superior também: '))
dlin(2, 25)
escreva(msg, tipo_linha, qnt_linha)
input()
escreva('<< FIM DO PROGRAMA >>', 1, 2)
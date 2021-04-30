import datetime
def voto(n):
    if n >= 65:
        print('O voto é opcional')
    if n >= 18 and n <= 64:
        print('O voto é obrigatorio')
    if n >= 16 and n <= 17:
        print('O voto é opcional')
    if n < 16:
        print('Não vota')

nasc = int(input('Ano de nascimento: '))
ano = datetime.date.today().year
idade = ano - nasc
print(f'Com {idade} anos: ',end='')
voto(idade)
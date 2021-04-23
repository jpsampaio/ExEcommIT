p = str(input('Quer começar? ')).strip().upper()[0]
homem = mulher = maiores = mumaior = 0
while p == 'S':
    i = int(input('Quantos anos? '))
    if i >= 18:
        maiores = maiores + 1
    s = str(input('Qual o gênero? (Masculino ou feminino)')).strip().upper()[0]
    if s == 'M':
        homem += 1
    elif s == 'F':
        mulher += 1
    while s != 'M' and s != 'F':
        s = str(input('Qual o gênero? (Masculino ou feminino)')).strip().upper()[0]
        if s == 'M':
            homem += 1
        elif s == 'F':
            mulher += 1
    if s == 'F':
        if i >= 18:
            mumaior += 1
    print('-=' * 30)
    p = str(input('Quer continuar?')).strip().upper()[0]
    print('-=' * 30)
    while p != 'S' and p != 'N':
        p = str(input('Quer continuar? ')).strip().upper()[0]
        print('-=' * 30)
    if p == 'N':
        break
print('Fim')
print('Ao todo tivemos:')
print(f'{maiores} maiores de idade')
print(f'{homem} homens ')
print(f'{mulher} mulheres')
print(f'E {mumaior} mulheres maiores de idade')
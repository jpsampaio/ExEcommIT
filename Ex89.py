alunos = list()
dados = list()
while True:
    dados.append(str(input('Nome: ').capitalize().strip()))
    dados.append(float(input('Nota 1: ')))
    dados.append(float(input('Nota 2: ')))
    alunos.append(dados[:])
    dados.clear()
    ask = str(input('Deseja continuar? [S/N]: ')).upper().strip()
    if ask in 'nN':
        break
a = 'NOME'
b = 'MÉDIA'
print('='*30)
print(f'N°{a:^20}{b:<20}')
print('-'*30)
for c,v in enumerate(alunos):
    print(f'{c}  {v[0]:^20}  {(v[1]+v[2])/2:<20}')
print('='*30)
while True:
    ask = int(input('Mostrar nota de qual aluno?[999 Encerra]: '))
    if ask == 999:
        break
    else:
        if ask >= len(alunos):
            print('Aluno não existe, digite um válido.')
        else:
            print(f'As notas de {alunos[ask][0]} são {alunos[ask][1]} e {alunos[ask][2]}')
print('<<= OBRIGADO VOLTE SEMPRE! =>>')
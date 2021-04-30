from datetime import date
ano = date.today().year
dicionario = {'Nome': str(input('Digite seu nome: ')), 'Idade': ano - int(input('Ano de nascimento: ')),
              'Carteira de trabalho': int(input('Carteira de trabalho (0 não tem): '))}
if dicionario['Carteira de trabalho'] != 0:
    dicionario['Ano de Contratação'] = int(input('Ano de contratação: '))
    dicionario['Salário'] = float(input('Salário R$'))
    if ano - dicionario['Idade'] < 62 or ano - dicionario['Ano de Contratação'] < 15:
        dicionario['Apostentadoria'] = f'Faltam {15 - (ano - dicionario["Ano de Contratação"])} anos.'
    else:
        dicionario['Apostentadoria'] = 'Você já pode se aposentar.'
print('--' * 20)
for k, v in dicionario.items():
    print(f'{k}: {v}')
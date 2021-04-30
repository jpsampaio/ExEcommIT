dados = dict()
gols = []
total = 0
dados['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
for c in range (0,partidas):
    n = int(input(f'Quantos gols na partida {c+1}: '))
    gols.append(n)
    total += n
dados['gols'] = gols
dados['total'] = total
print('=-'*30)
print(dados)
print('=-'*30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('=-'*30)
print(f'O Jogador {dados["nome"]} jogou {partidas} partidas')
for c in range (0, partidas):
    print(f'Na partida {c+1} ele fez {gols[c]} gols')
print(f'Foi um total de {total} gols! ')
from random import shuffle
print('Sequência de apresentação de trabalho:')
g1 = input('Digite um grupo:')
g2 = input('Digite um grupo:')
g3 = input('Digite um grupo:')
g4 = input('Digite um grupo:')
g5 = input('Digite um grupo:')
sequencia = [g1,g2,g3,g4,g5]
shuffle(sequencia)
print(f'A sequência de apresentação será:{sequencia}')
from time import sleep

def maior(*valores):
  maior = 0
  print('-=' * 30)
  print('Analisando valores passados..')
  for c in valores:
    print(f'{c}', end=" ", flush=True)
    sleep(1)
    if c > maior:
      maior = c
  print('')
  print(f'Foram informados {len(valores)} valores ao todo')
  print(f'O maior valor informado foi {maior}')

maior(2, 9 , 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
a = input('Digite algo, por favor')
print('O tipo primitivo desse valor é ', type(a))
print('Só tem espaços? ', a.isspace())
print('É um número? ', a.isnumeric())
print('É alfabético? ', a.isalpha())
print('É alfanumerico? ', a.isalnum())
print('Está em maiscúla? ', a.isupper())
print('Está em minúscula? ', a.islower())
print('Está em capitalizada? ', a.istitle())
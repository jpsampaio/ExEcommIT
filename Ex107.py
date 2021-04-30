ARQUIVO fileEx.py

import coin;

num = float(input('\nType a price (in R$): '));
coin.increase(num);
coin.decrease(num);
coin.half(num);
coin.double(num);


ARQUIVO coin.py

def increase(num):
	num += num * 0.1;
	print('\nIncreasing by 10%, we got R$ {:.2f}' .format(num));


def decrease(num):
	num -= num * 0.1;
	print('\nDecreasing by 10%, we got R$ {:.2f}' .format(num));


def half(num):
	num -= num/2;
	print(f'\nThe half of {(num * 2):.2f} it is R${(num):.2f}');


def double(num):
	num *= 2;
	print(f'\nThe double of {(num/2):.2f} it is R$ {(num):.2f}');
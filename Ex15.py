c = float(input('Quanto tempo você ficou com o carro:'))
d = float(input('Quantos Km rodou?'))
s = c*60
s1 = d*0.15
r = s + s1
print('O valor a ser pagar pelo veiculo incluindo os km e dias rodados é de R${:.2F}'.format(r))
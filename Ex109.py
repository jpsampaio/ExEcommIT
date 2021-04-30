def moeda(p, moeda='R$'):
    return '{}{:.2f}'.format(moeda, p).replace('.',',')  
    
def metade(p):
    res = moeda(p / 2)
    return res
    
def dobro(p):
    res = moeda(p * 2)
    return res
    
def aumento(p):
    res = moeda(p + (p * 10/100))
    return res

import ex109modulo

pre = float(input('Preço: R$'))
m = ex109modulo.moeda(pre)
met = ex109modulo.metade(pre)
d = ex109modulo.dobro(pre)
aum = ex109modulo.aumento(pre)
print('A metade de {} é {}'.format(m, met))
print('O dobro de {} é {}'.format(m, d))
print('Aumentando 10% temos {}'.format(aum))
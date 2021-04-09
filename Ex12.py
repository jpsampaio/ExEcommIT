prod = float(input('Qual o preço do produto: '))
pdesc = float(input('Qual a porcentagem de desconto: '))
vdesc = prod*pdesc/100
nprod = prod-vdesc
print('O valor com desconto é: {}'.format(nprod))


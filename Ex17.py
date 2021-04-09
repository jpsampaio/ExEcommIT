from math import pow
from math import sqrt
cateto_adj = float(input('Informe o comprimento em cm do cateto adjacente: '))  # Cateto ao lado do ângulo
cateto_opt = float(input('Informe o comprimento em cm do cateto oposto: '))  # Cateto em frente ao ângulo

# Formula: c = sqrt(a²+b²)
hipotenusa = sqrt(pow(cateto_adj, 2)+pow(cateto_opt, 2))
print('A hipotenusa tem o comprimento de: {:.2f} cms'.format(hipotenusa))
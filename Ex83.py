abre = []
fecha = []
exp = str(input('Digite uma expressão que use parenteses abaixo.\n>>>'))
for p, c in enumerate(exp):
    if '(' in exp[p]:
        abre.append(c)
    if ')' in exp[p]:
        fecha.append(c)
print('Expressão válida!' if len(abre) == len(fecha) else 'Expressão inválida!')
num = [ ]
pma = [ ]
pme = [ ]
for c in range(0, 5):
    num.append(int(input(f'Diga o valor da posição {c}: ')))
for n in range(0, len(num)):
    if num[n] == max(num):
        n = str(n)
        pma.append(n)
    else:
        if num[n] == min(num):
            n = str(n)
            pme.append(n)
pma = ', '.join(pma)
pme = ', '.join(pme)
print(num)
print(f'Posição dos:\nMaiores: {pma}\nMenores: {pme}')
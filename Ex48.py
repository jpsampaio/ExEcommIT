soma=0
s = c = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        c += 1
        s += n
print(f"A soma de todos os {c} valores solicitados é {s}.")
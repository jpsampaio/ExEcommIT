tgasto = 0
maiorMil = 0
b = 0
pbarato = " "
while True:
    p = input("Nome do produto===>")
    t = int(input("Preço R$"))
    if t>1000:
        maiorMil += 1
    if t<1000:
        pbarato = p
        b = t
    if t<b:
        b = t
        pbarato = p
    tgasto += t
    f = " "
    while f not in "SN":
        f = str(input("Deseja continuar?[S/N]: ")).upper().strip()[0]
    if f == "N":
        break

print("=" * 40)
print("Mercado Baratão")
print("=" * 40)
print(f"Total gasto {tgasto}")
print(f"{maiorMil} produtos custaram mais de 1000")
print(f"o produto mais barato foi {pbarato}")
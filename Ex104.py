def leiaint(txt):
    n = (input(f"{txt} \n"))
    while True:
        try:
            int(n)
            break

        except ValueError:
            print("Errou")
            n = input(f"{txt} \n")
    return n

a = leiaint('Digite um numero')
print(a)
cont = 1
soma = menor = maior = n = int(input("Digite um número: "))
resp = input("Quer continuar [S/N]: ").upper()
while resp == "S":
    n = int(input("Digite um número: "))
    soma += n
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
    cont += 1
    resp = input("Quer continuar [S/N]: ").upper()
print("Você digitou {} números e a média foi {:.2f}\nO maior valor foi {} e o menor valor foi {}".format(cont, soma/cont, maior, menor))
while True:

    n1 = float(input("\n   Escreva o lado 1 do triângulo: "))
    n2 = float(input("   Escreva o lado 2 do triângulo: "))
    n3 = float(input("   Escreva o lado 3 do triângulo: "))

    if(n1 > 0 and n2 > 0 and n3 > 0 and n1 <= n2+n3 and n2 <= n1+n3  and n3 <= n1+n2):
        if(n1 == n2 and n1 != n3 or n1 == n3 and n1 != n2 or n2 == n3 and n1 != n2):
            print("\n - O Triângulo é Isósceles !")
        elif(n1 == n2 and n2 == n3):
            print("\n - O Triângulo é Equilátero !")
        else:
            print("\n - O Triângulo é Escaleno !")
        print("-=-"*31)
    else:
        print("  -  Não pode formar um triângulo")


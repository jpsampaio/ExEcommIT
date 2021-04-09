frase = input('Digite uma frase: \n').strip()
n1 = frase.replace("ã","a").replace("á","a").replace("à","a").replace("â","a").upper().count("A")
n2 = frase.replace("ã","a").replace("á","a").replace("à","a").replace("â","a").upper().find("A")+1
n3 = frase.replace("ã","a").replace("á","a").replace("à","a").replace("â","a").upper().rfind("A")

print('A frase que você digitou foi: {}Sua frase tem {} letras (A), a primeira começa na posição {} e a última termina na posição {}' .format(frase,n1,n2,n3))


palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

v = ("a","e","i", "o", "u")

count = 0
for x in range (0,len(palavras)):
    for y in range(0,len(palavras[x])):
         if palavras[x][y] in v[:]:
            count +=1
    print (palavras[x], "Tem {} vogais.".format(count))
    count = 0
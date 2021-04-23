lst=[]  
for c in range(1, 6):
    peso=float(input('Peso da {}ª pessoa em KG: '.format(c)))
    lst+=[peso]   
print('')
print('O Maior peso foi:', max(lst))  
print('O Menor peso foi:', min(lst)) 
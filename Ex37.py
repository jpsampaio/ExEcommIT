n = int(input('Digite um número inteiro: '))
print(""""Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL""")
op = int(input('Sua opção: '))
if op == 1:
    potato = 'BINÁRIO'
    comp = bin(n)
    print(f'{n} convertido para {potato} fica {comp.replace("0b", "")}')
elif op == 2:
    potato = 'OCTAL'
    comp = oct(n)
    print(f'{n} convertido para OCTAL fica {comp.replace("0o","")}')
elif op == 3:
    comp = hex(n)
    print(f'{n} convertido para HEXADECIMAL fica {comp.replace("0x","")}')
else:
    print('ERRO! opção inválida, tem que se escolher números entre 1, 2, 3.')
    op = int(input('Digite uma opção válida: '))
    if op == 1:
        potato = 'BINÁRIO'
        comp = bin(n)
        print(f'{n} convertido para {potato} fica {comp.replace("0b", "")}')
    elif op == 2:
        potato = 'OCTAL'
        comp = oct(n)
        print(f'{n} convertido para OCTAL fica {comp.replace("0o", "")}')
    elif op == 3:
        comp = hex(n)
        print(f'{n} convertido para HEXADECIMAL fica {comp.replace("0x", "")}')
    else:
        print('Opção errada de novo krl')
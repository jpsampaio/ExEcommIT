print('='*10, 'Loja do João', '='*10)
preco = float(input('Preço das Compras: R$'))
print('FORMA DE PAGAMENTO'
      '\n[1] à vista dinheiro/cheque'
      '\n[2] à vista cartão'
      '\n[3] 2x no cartão'
      '\n[4] 3x ou mais no cartão.')
while True:
    opcao = int(input('Qual sua opção? '))
    if opcao == 1:
        desconto = preco*0.3
        print(f'Nesta forma de pagamento o valor R${preco} recebe um desconto de 10% igual a {preco - desconto}.')
        break
    elif opcao == 2:
        desconto = preco*0.5
        print(f'Nesta forma de pagamento o valor R${preco} recebe um desconto de 10% igual a {preco - desconto}.')
        break
    elif opcao == 3:
        print(f'Nesta forma de pagamento o valor R${preco} é o mesmo e será pago em duas parcelas de {preco/2}.')
        break
    elif opcao == 4:
        parcela = int(input('Gostaria de pagar em quantas parcelas?'))
        preco = (preco*0.3)+preco
        print(f'Nesta forma de pagamento o valor R${preco} será pago em {parcela} parcelas de {preco/parcela}.')
        break
    else:
        print('Opção inválida.')
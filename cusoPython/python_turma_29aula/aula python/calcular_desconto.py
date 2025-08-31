quant_itens = int(input("Quantos iténs vai comprar: "))
valor_item = 12.50
valor_final = quant_itens * valor_item

if quant_itens == 1:
    print("Valor da compra R$ ",valor_item)
elif quant_itens <= 5:
     valor_final *= (1 - 3/100)
     print(f"valor da compra R$ {valor_final:.2f} com desconto de 3%")
elif quant_itens <= 10:
    valor_final *= (1 - 5/100)
    print(f"valor da compra R$ {valor_final:.2f} com desconto de 5%")
else:
    valor_final *= (1 - 7/100)
    print(f"valor da compra R$ {valor_final:.2f} com desconto de 7%")
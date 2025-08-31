valor_do_pedido = 50.00
area_de_entrega = "Centro"
valor_total_pedido = float(input("Digite o valor total do pedido: "))
entrega = input("Digite a área de entrega: ").capitalize()

if valor_total_pedido >= valor_do_pedido and entrega == area_de_entrega:
    print("seu pedido será entregue.")
else:
    print("Desculpe, seu pedido não cumpre os requisitos de entrega.")


tipo_pizza = input("Sua pizza é DOCE ou SALGADA? ").upper()
tipo_recheio = input("Qual o recheio ? calabraza ou frango ").upper()

if tipo_pizza == "SALGADA" and (tipo_recheio == "CALABRESA" or tipo_recheio == "FRANGO"):
    print("Sua pizza pode seu feita!")
else:
    print("Você não tem os ingredientes corretos para esta receita,.")

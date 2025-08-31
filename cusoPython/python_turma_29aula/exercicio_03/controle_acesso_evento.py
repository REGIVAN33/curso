lista_vip = "SIM"
ingresso = "SIM"
resposta_vip = input("Você está na lista Vip? [SIM ou NÃO]").upper()
tem_ingresso =input("Você tem ingresso? [SIM ou NÃO]").upper()

if lista_vip == resposta_vip or ingresso == tem_ingresso:
    print("Enrada permitida!")
else:
    print("Entrada negada.")


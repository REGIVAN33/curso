idade_permitida = 16
idade = int(input("Escreva sua idade: "))

if not idade >= idade_permitida:
    print("Desculpe, você não tem idade suficiente para assistir este filme.")
else:
    print("Bom filme!")

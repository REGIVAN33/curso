# peso ideal para homem e mulher

nome = input("Digite seu nome: ")
sexo = input("Digite seu sexo [M | F]: ").upper()
altura = float(input("Digite sua altuta (em metros): "))
peso = float(input("Digite seu peso (em kg): "))

imc = peso / (altura ** 2)

if sexo == "F":
    peso_ideal = (62.1 * altura) - 44.7
elif sexo == "M":
    peso_ideal = (72.7 * altura) - 58
else:
    print("Opção de sexo inválida.")
    exit()

print(f"\nOlá, {nome}!")
print(f"Seu IMC é de {imc:.2f}.")
print(f"Seu peso ideal é de {peso_ideal:.2f} kg.")

if peso < peso_ideal:
    engordar = peso_ideal - peso
    print(f"Você está abaixo do peso ideal. Precisa engordar {engordar:.2f} kg.")
elif peso > peso_ideal:
    emagrecer = peso - peso_ideal
    print(f"Você está acima do peso ideal. Precisa emagrecer {emagrecer:.2f} kg.")
else:
    print("Você está com o peso ideal. Parabéns!")

if imc < 18.5:
    print("Classificação do IMC: Magreza")
elif 18.5 <= imc < 25:
    print("Classificação do IMC: Normal")
elif 25 <= imc < 30:
    print("Classificação do IMC: Sobrepeso")
elif 30 <= imc < 35:
    print("Classificação do IMC: Obesidade Grau I")
elif 35 <= imc < 40:
    print("Classificação do IMC: Obesidade Grau II")
else:
    print("Classificação do IMC: Obesidade Grau III (Mórbida)")
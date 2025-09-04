print(f"{'*' * 18} {'GRANDEZAS ELÉTRICAS '} {'*' * 18}")
print("1. Tensão (em Volt)")
print("2. Resistência (em Ohm)")
print("3. Corrente (em Ampére)")
print("*" * 48)
op = int(input("Qual grandeza deseja calcular? "))
if op < 1 or op > 3:
    print("Opção inválida.")
elif op == 1:
    R = float(input("Digite o valor da corrente (em Ohm): "))
    i = float(input("Digite o valor da corrente (em Ampére): "))
    U = R * i
    print(f"\nU = {U:.2f}")
elif op == 2:
    U = float(input("Digite o valor da tensão (em Volt): "))
    i = float(input("Digite o valor da corrente (em Ampére): "))
    R = U / i
    print(f"\nR = {R:.2f}")
else:
    U = float(input("Digite o valor da tensão (em Volt): "))
    R = float(input("Digite o valor da corrente (em Ohm): "))
    i = U / R
    print(f"\ni = {i:.2f}")
def calculadora():
    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            operacao = input("Digite a operação (+, -, *, /) ou 'sair' para fechar: ")

            if operacao.lower() == 'sair':
                print("Calculadora encerrada. Até mais!")
                break

            num2 = float(input("Digite o segundo número: "))

            if operacao == '+':
                resultado = num1 + num2
            elif operacao == '-':
                resultado = num1 - num2
            elif operacao == '*':
                resultado = num1 * num2
            elif operacao == '/':
                if num2 == 0:
                    print("Erro: Divisão por zero não é permitida.")
                    continue 
                else:
                    resultado = num1 / num2
            else:
                print("Operação inválida.")
                continue

            print(f"O resultado é: {resultado}")

        except ValueError:
            print("Entrada inválida. Por favor, digite apenas números.")
        
calculadora()
# Uma imobiliária paga aos seus corretores um salário base
#de R$ 1.500,00. Além disso, uma comissão de R$ 200,00 por
#cada imóvel vendido e 5% do valor de cada venda. Construa
#um programa que solicite o nome do corretor, a quantidade
#de imóveis vendidos e o valor total de suas vendas. Ao fim, o
#programa deve calcular e escrever o salário final do corretor de
#imóveis.

salario_base = 1500.00
comisao = 200.00
porcentagem_vendas = 0.05  
nome_corretor = input("Digite seu nome: ")
imoveis_vendidos = int(input("Informe a quantidade de imóveis vendidos: "))
total_vendas = float(input("Qual o valor total de suas vendas? "))

salario_final = salario_base + (imoveis_vendidos * comisao) + (total_vendas * porcentagem_vendas)

print(f"O salário final do corretor {nome_corretor} é de R$ {salario_final:.2f}.")
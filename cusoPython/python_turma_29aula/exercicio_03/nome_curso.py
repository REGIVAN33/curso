nome = "Regivan"
curso = "Python"
nome_digitado = input("Digite seu nome: ").capitalize()
curso_digitado = input("Digite o nome do curso: ").capitalize()

if nome == nome_digitado and curso == curso_digitado:
    print(nome_digitado,"Bem vindo a turma 29!")
else:
    print(nome_digitado,"Você não está matriculado.")
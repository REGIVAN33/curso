# Construa um programa que receba do usuário a variação do
# deslocamento de um objeto (em metros) e a variação do tempo
# percorrido (em segundo). Ao fim, o programa deve calcular a
# velocidade média, em m/s, do objeto.

variacao_deslocamento = float(input(" Digite a variação do deslocamento do objeto (em metros): "))
tempo_percorrido = float(input("Digite o tempo percorrido (em segundos): "))

velocidade_media = variacao_deslocamento / tempo_percorrido 
print(f"Vm = {velocidade_media:.2f} m/s")

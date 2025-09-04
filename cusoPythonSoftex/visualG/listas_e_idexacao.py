#Dada a lista numeros = [10, 20, 30, 40, 50], faça:
# Acesse e imprima o terceiro elemento
# Adicione o número 60 no final da lista
# Remova o número 20 da lista

numeros = [10, 20, 30, 40, 50]
print(f"O terceiro elemento da lista é {numeros[2]}")
numeros.append(60)
numeros.remove(20)
print(f"O terceiro elemento da lista agora é {numeros[2]}")
print(numeros)


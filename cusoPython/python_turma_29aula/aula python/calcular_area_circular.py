# Construa um programa para calcular a área de convivência
#de uma escola cujo formato é circular. Para isso, o usuário deve
#informar o valor do raio.

from math import pi

valor_raio = float(input("Informe o valor da área: "))

area = pi * valor_raio ** 2
print(f"Área = {area:.2f}.")
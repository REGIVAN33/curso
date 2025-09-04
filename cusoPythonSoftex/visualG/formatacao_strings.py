# formatação de strings

from datetime import datetime
ano_atual = datetime.now().year

clube = "SPFC"
campeonato_mundial = 3
ano_fundacao = 1930
print(f"{clube} possui {campeonato_mundial} títulos mundiais.")
print(F"São {ano_atual - ano_fundacao} anos de existência.") 

print(f"Matrícula do Charles Babbage é {25:06d}.")
print(F"Matrícula do Alan Turing é {99999:06d}.")
print(F"Matrícula da Ada Lovelace é {100387:06d}.")


print(F"Valor de pi é {3.14159265352384626433:.20f}.")
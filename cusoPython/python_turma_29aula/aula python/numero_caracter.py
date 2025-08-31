 #len() retorna o número de caracteres da string

nome = input("Digite seu nome completo: ")

if len(nome) > 50:
    print(f"Seu nome é grande, ele possui {len(nome)} letras. ")
else:
    print(f"Ele possui {len(nome)} caracteres.")
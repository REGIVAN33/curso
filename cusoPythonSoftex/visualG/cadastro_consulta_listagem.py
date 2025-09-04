def cadastramento():
    """
    Função para realizar o cadastramento
    """
    print("---Opção: Cadastramento ---")
    print("Realizando o cadastramento de uma nova consulta...")
    #Esperando o código para cadastro
    input("pressione <ENTER> para continuar")

def consulta():
    """Função para realizar consulta"""
    print("--- Opção: Consulta ---")
    print("realizando uma consulta...")
    #código de consulta aqui
    input("pressione <ENTER> para continuar.")

def listagem():
    """
    Função para gerar uma listagem com submenu.
    """
    print("--- Opção: Listagem ---")
    print("1 - Gerar relatório resumido")
    print("2 - Gerar relatório detalhado")
    print("3 - Voltar ao menu principal")
    
    try:
        sub_opcao = int(input("Escolha o tipo de relatório: "))
        if sub_opcao == 1:
            print("Gerando relatório resumido...")
            # Aqui entraria o código para gerar o relatório resumido
        elif sub_opcao == 2:
            print("Gerando relatório detalhado...")
            # Aqui entraria o código para gerar o relatório detalhado
        elif sub_opcao == 3:
            print("Voltando ao menu principal.")
            return # Sai da função e retorna para o loop principal
        else:
            print("Opção de relatório inválida.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")
    
    input("Pressione <ENTER> para continuar.")
    
def exibir_menu():
    """Função para exibir o menu de opcções"""
    print("=======================")
    print("    MENU PRINCIPAL   ")
    print("=======================")
    print("1 - Cadastramento")
    print("2 - Cosulta")
    print("3 - Listagem")
    print("4 - Fim")
    print("=======================")

def main():
    """função principal que gerencia o fluxo do programa"""

    opcao = 0
    while opcao != 4:
        exibir_menu()
        try:
            opcao = int(input("Escolha a sua opção: "))
            if opcao == 1:
                cadastramento()
            elif opcao == 2:
                consulta()
            elif opcao == 3:
                listagem()
            elif opcao == 4:
                print("programa encerrado, Até mais")
            else:
                print("Opção inválida. Escolha uma opção de 1 a 4.")
        except ValueError:
            print("Entrada inválid. Por favor, digite um número.")
if __name__ == "__main__":
    main()
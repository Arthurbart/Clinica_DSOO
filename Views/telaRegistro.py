class TelaRegistro():

    def mostrar_opcoes(self):
        print("\n===== REGISTROS =====")
        print("1 - Atendimentos")
        print("2 - Procedimentos")
        print("3 - Pagamentos")
        print("4 - Voltar")

        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            print("Digite apenas números.")
            return 0

    

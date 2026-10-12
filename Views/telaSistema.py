class TelaSistema():

    def mostrar_opcoes(self):
        print("\n===== SISTEMA DE CLÍNICAS =====")
        print("1 - Novo Cadastro")
        print("2 - Novo Registro")
        print("3 - Relatório")
        print("4 - Fechar")

        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            print("Digite apenas números.")
            return 0
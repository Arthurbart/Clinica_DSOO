class TelaCadastro():

    def mostrar_opcoes(self):
        print("\n===== CADASTROS =====")
        print("1 - Paciente")
        print("2 - Profissional")
        print("3 - Clínica")
        print("4 - Tipo de Atendimento")
        print("5 - Voltar")

        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            print("Digite apenas números.")
            return 0
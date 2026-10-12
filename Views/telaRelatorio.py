class TelaRelatorio():

    def mostrar_opcoes(self):
        print("\n===== RELATÓRIOS =====")
        print("1 - Clínicas com maior número de atendimentos")
        print("2 - Atendimentos mais caros e mais baratos")
        print("3 - Procedimentos mais realizados")
        print("4 - Procedimentos mais caros e mais baratos")
        print("5 - Voltar")

        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            print("Digite apenas números.")
            return 0

    def mostra_mensagem(self, mensagem):
        print(mensagem)
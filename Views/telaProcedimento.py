class TelaProcedimento():
    def __init__(self):
        pass

    def mostrar_opcoes(self):
        print("\n===== PROCEDIMENTO =====")
        print("1 - Cadastrar procedimento")
        print("2 - Listar procedimentos")
        print("3 - Editar procedimento")
        print("4 - Excluir procedimento")
        print("5 - Voltar")

        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            print("Digite apenas números.")
            return 0

    def pega_dados_procedimento(self):
        descricao = input("Digite a descrição do procedimento: ")

        try:
            custo = float(input("Digite o custo do procedimento: "))
        except ValueError:
            print("Digite um custo numérico válido.")
            return None

        profissional = input(
            "Digite o CPF do profissional responsável pelo procedimento: "
        )

        return {
            "descricao": descricao,
            "custo": custo,
            "profissional": profissional
        }

    def seleciona_procedimento(self, procedimentos):
        print("\n===== PROCEDIMENTOS =====")

        for i, procedimento in enumerate(procedimentos):
            print(
                f"{i + 1} - "
                f"{procedimento.descricao} | "
                f"R$ {procedimento.custo:.2f} | "
                f"Profissional: {procedimento.profissional.nome}"
            )

        try:
            opcao = int(input("Digite o número do procedimento: "))
        except ValueError:
            print("Digite apenas números.")
            return None

        if opcao < 1 or opcao > len(procedimentos):
            return None

        return procedimentos[opcao - 1]

    def mostra_mensagem(self, mensagem):
        print(mensagem)
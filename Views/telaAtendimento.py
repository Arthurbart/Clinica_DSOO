class TelaAtendimento():
    def __init__(self):
        pass

    def mostrar_opcoes(self):
        print("\n===== ATENDIMENTOS =====")
        print("1 - Cadastrar atendimento")
        print("2 - Listar atendimentos")
        print("3 - Editar atendimento")
        print("4 - Excluir atendimento")
        print("5 - Voltar")

        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            print("Digite apenas números.")
            return 0

    def pega_dados_atendimento(self):
        data = input("Digite a data do atendimento (dd/mm/aaaa): ")
        horainicio = input("Digite a hora do início do atendimento (hh:mm): ")
        horafim = input("Digite a hora do fim do atendimento (hh:mm): ")

        try:
            valor = float(input("Digite o valor do atendimento: "))
        except ValueError:
            print("Digite um valor numérico válido.")
            return None

        return {
            "data": data,
            "horario_inicio": horainicio,
            "horario_fim": horafim,
            "valor": valor
        }

    def seleciona_atendimento(self, atendimentos):
        print("\n===== ATENDIMENTOS =====")

        for i, atendimento in enumerate(atendimentos):
            print(
                f"{i + 1} - "
                f"{atendimento.paciente.nome} | "
                f"{atendimento.data} | "
                f"{atendimento.clinica.nome} | "
                f"R$ {atendimento.valor:.2f}"
            )

        try:
            opcao = int(input("Digite o número do atendimento: "))
        except ValueError:
            print("Digite apenas números.")
            return None

        if opcao < 1 or opcao > len(atendimentos):
            return None

        return atendimentos[opcao - 1]

    def mostra_mensagem(self, mensagem):
        print(mensagem)

    def pede_por_procedimento(self):
        return input("Foi feito algum procedimento? (s/n): ")

    def seleciona_tipo_atendimento(self):
        return input("Digite o nome do tipo de atendimento: ")

    def seleciona_paciente(self):
        return input("Digite o CPF do paciente: ")

    def seleciona_profissional(self):
        return input("Digite o CPF do profissional: ")

    def seleciona_clinica(self):
        return input("Digite o nome da clínica: ")
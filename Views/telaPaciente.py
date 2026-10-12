class TelaPaciente():
    def mostrar_opcoes(self):
        print("\n===== PACIENTE =====")
        print("1 - Cadastrar paciente")
        print("2 - Listar pacientes")
        print("3 - Editar paciente")
        print("4 - Excluir paciente")
        print("5 - Voltar")
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            print("Digite apenas números.")
            return 0

    def pega_dados_paciente(self):
        nome = input("Digite o nome do paciente: ")
        celular = input("Digite o celular do paciente: ")
        cpf = input("Digite o CPF do paciente: ")
        idade = int(input("Digite a idade do paciente: "))
        return {"nome": nome, "celular": celular, "cpf": cpf, "idade": idade}

    def seleciona_paciente_por_cpf(self):
        return input("Digite o CPF do paciente: ")

    def mostra_mensagem(self, mensagem):
        print(mensagem)
class TelaProfissional():
    def mostrar_opcoes(self):
        print("\n===== PROFISSIONAL =====")
        print("1 - Cadastrar profissional")
        print("2 - Listar profissionais")
        print("3 - Editar profissional")
        print("4 - Excluir profissional")
        print("5 - Voltar")
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            print("Digite apenas números.")
            return 0

    def pega_dados_profissional(self):
        nome = input("Digite o nome do profissional: ")
        celular = input("Digite o celular do profissional: ")
        cpf = input("Digite o CPF do profissional: ")
        especialidade = input("Digite a especialidade do profissional: ")
        registro_profissional = input("Digite o registro profissional do profissional: ")
        return {"nome": nome, "celular": celular, "cpf": cpf, "especialidade": especialidade, "registro_profissional": registro_profissional}

    def seleciona_profissional_por_cpf(self):
        return input("Digite o CPF do profissional: ")

    def mostra_mensagem(self, mensagem):
        print(mensagem)
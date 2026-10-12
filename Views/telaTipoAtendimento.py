class TelaTipoAtendimento():
    def mostrar_opcoes(self):
        print("\n===== TIPO DE ATENDIMENTO =====")
        print("1 - Cadastrar tipo de atendimento")
        print("2 - Listar tipos de atendimento")
        print("3 - Editar tipo de atendimento")
        print("4 - Excluir tipo de atendimento")
        print("5 - Voltar")

        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            print("Digite apenas números.")
            return 0

    def pega_dados_tipo_atendimento(self):
        nome = input("Digite o nome do tipo de atendimento: ")
        descricao = input("Digite a descrição do tipo de atendimento: ")
        return {"nome": nome, "descricao": descricao}

    def seleciona_tipo_atendimento_por_nome(self):
        return input("Digite o nome do tipo de atendimento: ")

    def mostra_mensagem(self, mensagem):
        print(mensagem)
class TelaClinica():
    def mostrar_opcoes(self):
        print("\n===== CLÍNICA =====")
        print("1 - Cadastrar clínica")
        print("2 - Listar clínicas")
        print("3 - Editar clínica")
        print("4 - Excluir clínica")
        print("5 - Voltar")

        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            print("Digite apenas números.")
            return 0

    def pega_dados_clinica(self):
        nome = input("Digite o nome da clínica: ")
        localizacao = input("Digite a localização da clínica: ")
        descricao = input("Digite a descrição da clínica: ")
        horario_abertura = input("Digite o horário de abertura (HH:MM): ")
        horario_fechamento = input("Digite o horário de fechamento (HH:MM): ")

        return {
            "nome": nome,
            "localizacao": localizacao,
            "descricao": descricao,
            "horario_abertura": horario_abertura,
            "horario_fechamento": horario_fechamento
        }

    def seleciona_clinica_por_nome(self):
        return input("Digite o nome da clínica: ")

    def mostra_mensagem(self, mensagem):
        print(mensagem)
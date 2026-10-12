class TelaPagamento():

    def mostrar_opcoes(self):
        print("\n===== PAGAMENTOS =====")
        print("1 - Listar pagamentos")
        print("2 - Realizar pagamento")
        print("3 - Excluir pagamento")
        print("4 - Voltar")

        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            print("Digite apenas números.")
            return 0

    def mostrar_opcoes_novo_pagamento(self):
        print("\n===== PAGAMENTO =====")
        print("1 - Dinheiro")
        print("2 - PIX")
        print("3 - Cartão")

        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            print("Digite apenas números.")
            return 0

    def pega_dados_dinheiro(self, data_atendimento):

        data_formatada = data_atendimento.strftime("%d/%m/%Y")
        
        data = input(
            "Data do primeiro/único pagamento "
            "(lembrando que só pode ser feito pagamentos até o dia "
            f"{data_formatada}): "
        )


        return {
            "data": data
        }

    def pega_dados_cartao(self, data_atendimento):

        data_formatada = data_atendimento.strftime("%d/%m/%Y")
        
        data = input(
            "Data do primeiro/único pagamento "
            "(lembrando que só pode ser feito pagamentos até o dia "
            f"{data_formatada}): "
        )
        

        numero_cartao = input("Digite o número do cartão: ")
        bandeira = input("Digite a bandeira do cartão: ")

        return {
            "data": data,
            "numero_cartao": numero_cartao,
            "bandeira": bandeira
        }

    def pega_dados_pix(self, data_atendimento):

        data_formatada = data_atendimento.strftime("%d/%m/%Y")
        
        data = input(
            "Data do primeiro/único pagamento "
            "(lembrando que só pode ser feito pagamentos até o dia "
            f"{data_formatada}): "
        )

        cpf_pagador = input("Digite o CPF do pagador: ")

        return {
            "data": data,
            "cpf_pagador": cpf_pagador
        }

    def pega_dados_edicao_pagamento(self):
        data = input("Digite a nova data do pagamento (dd/mm/aaaa): ")

        try:
            valor_pago = float(input("Digite o novo valor pago: "))
        except ValueError:
            print("Digite um valor numérico válido.")
            return None

        return {
            "data": data,
            "valor_pago": valor_pago
        }

    def seleciona_pagamento(self, pagamentos):
        print("\n===== PAGAMENTOS =====")

        for i, pagamento in enumerate(pagamentos):
            print(
                f"{i + 1} - "
                f"{pagamento.paciente.nome} | "
                f"{pagamento.data} | "
                f"R$ {pagamento.valor_pago:.2f}"
            )

        try:
            opcao = int(input("Digite o número do pagamento: "))
        except ValueError:
            print("Digite apenas números.")
            return None

        if opcao < 1 or opcao > len(pagamentos):
            return None

        return pagamentos[opcao - 1]

    def mostra_mensagem(self, mensagem):
        print(mensagem)

    def mostra_pagamento(self, pagamento):
        print("\n===== PAGAMENTO =====")
        print(f"Paciente: {pagamento.paciente.nome}")
        print(f"Data do último pagamento: {pagamento.data.strftime('%d/%m/%Y')}")
        print(f"Valor restante: R$ {pagamento.valor_pago:.2f}")
        print(f"Forma de pagamento: {pagamento.forma_pagamento()}")

    def pega_nova_data_pagamento(self):
        return input(
            "Informe uma nova data para o pagamento (DD/MM/AAAA): "
        )

        
    def pega_dados_realizar_pagamento(self):
        data = input(
            "Data deste pagamento (DD/MM/AAAA): "
        )

        try:
            valor = float(input("Valor pago: R$ "))
        except ValueError:
            raise ValueError("Digite um valor numérico válido.")

        return {
            "data": data,
            "valor": valor
        }

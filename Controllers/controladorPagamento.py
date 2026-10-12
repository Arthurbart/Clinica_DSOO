from Views.telaPagamento import TelaPagamento
from Models.pagamentoDinheiro import PagamentoDinheiro
from Models.pagamentoPix import PagamentoPix
from Models.pagamentoCartao import PagamentoCartao
from datetime import datetime


class ControladorPagamento():
    def __init__(self):
        self.__tela_pagamento = TelaPagamento()
        self.__pagamentos = []

    
    def abre_tela(self):
        continua = True

        while continua:
            opcao = self.__tela_pagamento.mostrar_opcoes()

            if opcao == 1:
                self.listar_pagamentos()

            elif opcao == 2:
                self.realizar_pagamento()

            elif opcao == 3:
                self.excluir_pagamento()

            elif opcao == 4:
                continua = False

            else:
                self.__tela_pagamento.mostra_mensagem(
                    "Opção inválida."
                )


    def cadastrar_pagamento(self, atendimento):
        valor_total = atendimento.valor

        opcao = self.__tela_pagamento.mostrar_opcoes_novo_pagamento()

        if opcao == 1:
            return self.cadastrar_dinheiro(atendimento, valor_total)

        elif opcao == 2:
            return self.cadastrar_pix(atendimento, valor_total)

        elif opcao == 3:
            return self.cadastrar_cartao(atendimento, valor_total)

        else:
            self.__tela_pagamento.mostra_mensagem("Opção inválida.")
            return False

    def cadastrar_dinheiro(self, atendimento, valor_total):
        try:
            dados = self.__tela_pagamento.pega_dados_dinheiro(data_atendimento=atendimento.data)

            data_pagamento = self.obter_data_pagamento_valida(
                dados["data"], atendimento
            )

            pagamento = PagamentoDinheiro(
                data_pagamento,
                atendimento,
                atendimento.paciente,
                valor_total
            )

            self.__pagamentos.append(pagamento)

            self.__tela_pagamento.mostra_mensagem(
                "Pagamento em dinheiro cadastrado com sucesso!"
            )

            return True

        except ValueError as erro:
            self.__tela_pagamento.mostra_mensagem(str(erro))
            return False

    def cadastrar_cartao(self, atendimento, valor_total):
        try:
            dados = self.__tela_pagamento.pega_dados_cartao(data_atendimento=atendimento.data)

            data_pagamento = self.obter_data_pagamento_valida(
                dados["data"], atendimento
            )

            pagamento = PagamentoCartao(
                data_pagamento,
                atendimento,
                atendimento.paciente,
                valor_total,
                dados["numero_cartao"],
                dados["bandeira"]
            )

            self.__pagamentos.append(pagamento)

            self.__tela_pagamento.mostra_mensagem(
                "Pagamento em cartão cadastrado com sucesso!"
            )

            return True

        except ValueError as erro:
            self.__tela_pagamento.mostra_mensagem(str(erro))
            return False

    def cadastrar_pix(self, atendimento, valor_total):
        try:
            dados = self.__tela_pagamento.pega_dados_pix(data_atendimento=atendimento.data)

            data_pagamento = self.obter_data_pagamento_valida(
                dados["data"], atendimento
            )

            pagamento = PagamentoPix(
                data_pagamento,
                atendimento,
                atendimento.paciente,
                valor_total,
                dados["cpf_pagador"]
            )

            self.__pagamentos.append(pagamento)

            self.__tela_pagamento.mostra_mensagem(
                "Pagamento via PIX cadastrado com sucesso!"
            )

            return True

        except ValueError as erro:
            self.__tela_pagamento.mostra_mensagem(str(erro))
            return False

    def listar_pagamentos(self):
        if not self.__pagamentos:
            self.__tela_pagamento.mostra_mensagem(
                "Nenhum pagamento cadastrado."
            )
            return

        for pagamento in self.__pagamentos:
            self.__tela_pagamento.mostra_pagamento(pagamento)
    
    def excluir_pagamento(self):
        if not self.__pagamentos:
            self.__tela_pagamento.mostra_mensagem(
                "Nenhum pagamento cadastrado."
            )
            return

        pagamento = self.__tela_pagamento.seleciona_pagamento(
            self.__pagamentos
        )

        if pagamento is None:
            self.__tela_pagamento.mostra_mensagem(
                "Pagamento não encontrado."
            )
            return

        self.__pagamentos.remove(pagamento)

        self.__tela_pagamento.mostra_mensagem(
            "Pagamento excluído com sucesso!"
        )

    def encontrar_pagamento_por_atendimento(self, atendimento):
        for pagamento in self.__pagamentos:
            if pagamento.atendimento == atendimento:
                return pagamento
        return None

    def atualizar_valor_pagamento(self, atendimento, valor_anterior):
        pagamento = self.encontrar_pagamento_por_atendimento(atendimento)

        if pagamento is not None:
            valor_ja_pago = valor_anterior - pagamento.valor_pago

            novo_saldo = atendimento.valor - valor_ja_pago

            pagamento.valor_pago = round(max(0, novo_saldo), 2)

    def excluir_pagamento_por_atendimento(self, atendimento):
        pagamento = self.encontrar_pagamento_por_atendimento(atendimento)

        if pagamento is not None:
            self.__pagamentos.remove(pagamento)

    def validar_data_pagamento(self, data_pagamento, atendimento):
        try:
            if isinstance(data_pagamento, str):
                data_pagamento = datetime.strptime(
                    data_pagamento, "%d/%m/%Y"
                ).date()

            data_atendimento = atendimento.data

            if isinstance(data_atendimento, str):
                data_atendimento = datetime.strptime(
                    data_atendimento, "%d/%m/%Y"
                ).date()

            if data_pagamento >= data_atendimento:
                raise ValueError(
                    "A data do pagamento deve ser anterior à data do atendimento."
                )

            return data_pagamento

        except ValueError as erro:
            if "A data do pagamento deve ser anterior" in str(erro):
                raise

            raise ValueError(
                "Data inválida! Digite no formato DD/MM/AAAA."
            )
        
    def obter_data_pagamento_valida(self, data, atendimento):
        while True:
            try:
                return self.validar_data_pagamento(data, atendimento)

            except ValueError as erro:
                self.__tela_pagamento.mostra_mensagem(str(erro))
                data = self.__tela_pagamento.pega_nova_data_pagamento()

    
    def realizar_pagamento(self):
        if not self.__pagamentos:
            self.__tela_pagamento.mostra_mensagem(
                "Não existem pagamentos pendentes."
            )
            return

        pagamento = self.__tela_pagamento.seleciona_pagamento(
            self.__pagamentos
        )

        if pagamento is None:
            self.__tela_pagamento.mostra_mensagem(
                "Pagamento não encontrado."
            )
            return

        if pagamento.valor_pago == 0:
            self.__tela_pagamento.mostra_mensagem(
                "Este atendimento já está quitado."
            )
            return

        try:
            dados = self.__tela_pagamento.pega_dados_realizar_pagamento()

            data_pagamento = self.validar_data_pagamento(
                dados["data"], pagamento.atendimento
            )

            valor = float(dados["valor"])

            if valor <= 0:
                raise ValueError(
                    "O valor do pagamento deve ser maior que zero."
                )

            if valor > pagamento.valor_pago:
                raise ValueError(
                    f"O valor informado ultrapassa o saldo restante "
                    f"de R$ {pagamento.valor_pago:.2f}."
                )

            pagamento.valor_pago -= valor
            pagamento.data = data_pagamento

            pagamento.valor_pago = round(pagamento.valor_pago, 2)

            if pagamento.valor_pago == 0:
                self.__tela_pagamento.mostra_mensagem(
                    "Atendimento quitado! Não há mais saldo pendente."
                )
            
            else:
                self.__tela_pagamento.mostra_mensagem(
                    f"Pagamento realizado com sucesso!\n"
                    f"Valor restante: R$ {pagamento.valor_pago:.2f}"
                )

        except ValueError as erro:
            self.__tela_pagamento.mostra_mensagem(str(erro))

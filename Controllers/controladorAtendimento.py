from Views.telaAtendimento import TelaAtendimento
from Models.atendimento import Atendimento
from datetime import datetime

class ControladorAtendimento():
    def __init__(self, controlador_procedimentos, controlador_tipo_atendimento, controlador_paciente, controlador_profissional, controlador_clinica, controlador_pagamentos):
        self.__tela_atendimento = TelaAtendimento()
        self.__atendimentos = []
        self.__controlador_procedimentos = controlador_procedimentos
        self.__controlador_tipo_atendimento = controlador_tipo_atendimento
        self.__controlador_paciente = controlador_paciente
        self.__controlador_profissional = controlador_profissional
        self.__controlador_clinica = controlador_clinica
        self.__controlador_pagamentos = controlador_pagamentos

    def abre_tela(self):
        continua = True
        while continua:
            opcao = self.__tela_atendimento.mostrar_opcoes()

            if opcao == 1:
                self.cadastrar_atendimento()
            elif opcao == 2:
                self.listar_atendimentos()
            elif opcao == 3:
                self.editar_atendimento()
            elif opcao == 4:
                self.excluir_atendimento()
            elif opcao == 5:
                continua = False

    def obter_atendimentos(self):
        return self.__atendimentos

    def cadastrar_atendimento(self):

        dados_atendimento = self.__tela_atendimento.pega_dados_atendimento()

        cpf_paciente = self.__tela_atendimento.seleciona_paciente()

        paciente = self.__controlador_paciente.encontrar_paciente_por_cpf(
            cpf_paciente
        )

        if paciente is None:
            self.__tela_atendimento.mostra_mensagem(
                "Não é possível cadastrar atendimento sem um paciente cadastrado."
            )
            return

        cpf_profissional = self.__tela_atendimento.seleciona_profissional()

        profissional = self.__controlador_profissional.encontrar_profissional_por_cpf(
            cpf_profissional
        )

        if profissional is None:
            self.__tela_atendimento.mostra_mensagem(
                "Não é possível cadastrar atendimento sem um profissional cadastrado."
            )
            return

        nome_clinica = self.__tela_atendimento.seleciona_clinica()
        clinica = self.__controlador_clinica.encontrar_clinica_por_nome(nome_clinica)

        if clinica is None:
            self.__tela_atendimento.mostra_mensagem(
                "Não é possível cadastrar atendimento sem uma clínica cadastrada."
            )
            return

        nome_tipo = self.__tela_atendimento.seleciona_tipo_atendimento()

        tipo_atendimento = (
            self.__controlador_tipo_atendimento
            .encontrar_tipo_atendimento_por_nome(nome_tipo)
        )

        if tipo_atendimento is None:
            self.__tela_atendimento.mostra_mensagem(
                "Não é possível cadastrar atendimento sem tipo de atendimento."
            )
            return

        dados_validos = self.validar_data_horarios(
            dados_atendimento, clinica
        )

        if dados_validos is None:
            return

        data, horario_inicio, horario_fim = dados_validos

        procedimentos = self.registrar_procedimentos()

        try:
            valor_atendimento = float(dados_atendimento["valor"])
            if valor_atendimento < 0:
                raise ValueError("O valor do atendimento não pode ser negativo.")
        except ValueError as erro:
            self.__tela_atendimento.mostra_mensagem(str(erro))
            return

        valor_procedimentos = 0

        for procedimento in procedimentos:
            valor_procedimentos += procedimento.custo

        valor_total = valor_atendimento + valor_procedimentos

        atendimento = Atendimento(
            clinica,
            paciente,
            profissional,
            data,
            horario_inicio,
            horario_fim,
            tipo_atendimento,
            valor_atendimento,
            valor_procedimentos,
            valor_total,
            procedimentos
        )

        if valor_total > 0:
            pagamento_cadastrado = (
                self.__controlador_pagamentos.cadastrar_pagamento(atendimento)
            )

            if not pagamento_cadastrado:
                self.__tela_atendimento.mostra_mensagem(
                    "Atendimento não cadastrado porque o pagamento não foi concluído."
                )
                return

        self.__atendimentos.append(atendimento)

        self.__tela_atendimento.mostra_mensagem(
            "Atendimento cadastrado com sucesso!"
        )

    def listar_atendimentos(self):
        if not self.__atendimentos:
            self.__tela_atendimento.mostra_mensagem(
                "Nenhum atendimento cadastrado."
            )
            return

        for atendimento in self.__atendimentos:

            self.__tela_atendimento.mostra_mensagem(
                f"\n===== ATENDIMENTO =====\n"
                f"Paciente: {atendimento.paciente.nome}\n"
                f"Profissional: {atendimento.profissional.nome}\n"
                f"Clínica: {atendimento.clinica.nome}\n"
                f"Data: {atendimento.data.strftime('%d/%m/%Y')}\n"
                f"Início: {atendimento.horario_inicio.strftime('%H:%M')}\n"
                f"Fim: {atendimento.horario_fim.strftime('%H:%M')}\n"
                f"Tipo: {atendimento.tipo_atendimento.nome}\n"
                f"Valor atendimento: R$ {atendimento.valor_atendimento:.2f}\n"
                f"Valor procedimentos: R$ {atendimento.valor_procedimentos:.2f}\n"
                f"Valor total: R$ {atendimento.valor:.2f}"
            )

            pagamento = (
                self.__controlador_pagamentos.encontrar_pagamento_por_atendimento(atendimento)
            )

            valor_restante = (
                pagamento.valor_pago if pagamento is not None else 0
            )

            self.__tela_atendimento.mostra_mensagem(
                f"Valor restante para pagar: R$ {valor_restante:.2f}"
            )

            if atendimento.procedimentos:
                self.__tela_atendimento.mostra_mensagem(
                    "Procedimentos:"
                )

                for procedimento in atendimento.procedimentos:
                    self.__tela_atendimento.mostra_mensagem(
                        f"  - {procedimento.descricao} | "
                        f"R$ {procedimento.custo:.2f} | "
                        f"Profissional: {procedimento.profissional.nome}"
                    )
            else:
                self.__tela_atendimento.mostra_mensagem(
                    "Procedimentos: Nenhum"
                )

            if pagamento is not None:
                self.__tela_atendimento.mostra_mensagem(
                    f"Forma de pagamento: {pagamento.forma_pagamento()}"
                )

    def editar_atendimento(self):
        atendimento = self.__tela_atendimento.seleciona_atendimento(
            self.__atendimentos
        )

        if atendimento is None:
            self.__tela_atendimento.mostra_mensagem(
                "Atendimento não encontrado."
            )
            return

        valor_anterior = atendimento.valor

        dados_atendimento = self.__tela_atendimento.pega_dados_atendimento()

        cpf_paciente = self.__tela_atendimento.seleciona_paciente()
        paciente = self.__controlador_paciente.encontrar_paciente_por_cpf(cpf_paciente)

        if paciente is None:
            self.__tela_atendimento.mostra_mensagem(
                "Paciente não encontrado."
            )
            return

        cpf_profissional = self.__tela_atendimento.seleciona_profissional()
        profissional = self.__controlador_profissional.encontrar_profissional_por_cpf(cpf_profissional)

        if profissional is None:
            self.__tela_atendimento.mostra_mensagem(
                "Profissional não encontrado."
            )
            return

        nome_clinica = self.__tela_atendimento.seleciona_clinica()
        clinica = self.__controlador_clinica.encontrar_clinica_por_nome(nome_clinica)

        if clinica is None:
            self.__tela_atendimento.mostra_mensagem(
                "Clínica não encontrada."
            )
            return

        nome_tipo = self.__tela_atendimento.seleciona_tipo_atendimento()
        tipo_atendimento = self.__controlador_tipo_atendimento.encontrar_tipo_atendimento_por_nome(nome_tipo)

        if tipo_atendimento is None:
            self.__tela_atendimento.mostra_mensagem(
                "Tipo de atendimento não encontrado."
            )
            return

        dados_validos = self.validar_data_horarios(
            dados_atendimento, clinica
        )

        if dados_validos is None:
            return

        data, horario_inicio, horario_fim = dados_validos

        atendimento.paciente = paciente
        atendimento.profissional = profissional
        atendimento.clinica = clinica
        atendimento.data = data
        atendimento.horario_inicio = horario_inicio
        atendimento.horario_fim = horario_fim
        atendimento.tipo_atendimento = tipo_atendimento
        try:
            valor_atendimento = float(dados_atendimento["valor"])
            if valor_atendimento < 0:
                raise ValueError("O valor do atendimento não pode ser negativo.")
        except ValueError as erro:
            self.__tela_atendimento.mostra_mensagem(str(erro))
            return

        valor_procedimentos = 0

        for procedimento in atendimento.procedimentos:
            valor_procedimentos += procedimento.custo

        valor_total = valor_atendimento + valor_procedimentos

        atendimento.valor_atendimento = valor_atendimento
        atendimento.valor_procedimentos = valor_procedimentos
        atendimento.valor = valor_total

        self.__controlador_pagamentos.atualizar_valor_pagamento(atendimento, valor_anterior)

        self.__tela_atendimento.mostra_mensagem(
            "Atendimento editado com sucesso!"
        )

    def excluir_atendimento(self):
        atendimento = self.__tela_atendimento.seleciona_atendimento(
            self.__atendimentos
        )

        if atendimento is None:
            self.__tela_atendimento.mostra_mensagem(
                "Atendimento não encontrado."
            )
            return

        self.__controlador_pagamentos.excluir_pagamento_por_atendimento(
            atendimento
        )

        self.__controlador_procedimentos.excluir_procedimentos_por_atendimento(
            atendimento
        )

        self.__atendimentos.remove(atendimento)

        self.__tela_atendimento.mostra_mensagem(
            "Atendimento, procedimentos e pagamento excluídos com sucesso!"
        )

    def registrar_procedimentos(self):
        procedimentos = []

        resposta = self.__tela_atendimento.pede_por_procedimento()

        while resposta.lower() == "s":
            procedimento = self.__controlador_procedimentos.cadastrar_procedimento_por_atendimento()

            if procedimento is not None:
                procedimentos.append(procedimento)

            resposta = self.__tela_atendimento.pede_por_procedimento()

        if not procedimentos:
            self.__tela_atendimento.mostra_mensagem(
                "Nenhum procedimento foi registrado."
            )

        return procedimentos

    def atualizar_procedimento(self, procedimento):
        for atendimento in self.__atendimentos:
            if procedimento in atendimento.procedimentos:
                valor_anterior = atendimento.valor
                valor_procedimentos = 0

                for procedimento_atual in atendimento.procedimentos:
                    valor_procedimentos += procedimento_atual.custo

                atendimento.valor_procedimentos = valor_procedimentos
                atendimento.valor = (
                    atendimento.valor_atendimento + valor_procedimentos
                )

                self.__controlador_pagamentos.atualizar_valor_pagamento(
                    atendimento, valor_anterior
                )


    def remover_procedimento(self, procedimento):
        for atendimento in self.__atendimentos:
            if procedimento in atendimento.procedimentos:
                valor_anterior = atendimento.valor

                atendimento.procedimentos.remove(procedimento)

                valor_procedimentos = 0

                for procedimento_atual in atendimento.procedimentos:
                    valor_procedimentos += procedimento_atual.custo

                atendimento.valor_procedimentos = valor_procedimentos
                atendimento.valor = (
                    atendimento.valor_atendimento + valor_procedimentos
                )

                self.__controlador_pagamentos.atualizar_valor_pagamento(
                    atendimento, valor_anterior
                )

    def validar_data_horarios(self, dados, clinica):
        try:
            data = datetime.strptime(
                dados["data"], "%d/%m/%Y"
            ).date()

            horario_inicio = datetime.strptime(
                dados["horario_inicio"], "%H:%M"
            ).time()

            horario_fim = datetime.strptime(
                dados["horario_fim"], "%H:%M"
            ).time()

        except ValueError:
            self.__tela_atendimento.mostra_mensagem(
                "Data ou horário inválido. Use DD/MM/AAAA e HH:MM."
            )
            return None

        if horario_inicio >= horario_fim:
            self.__tela_atendimento.mostra_mensagem(
                "O horário de início deve ser anterior ao horário de término."
            )
            return None

        if (horario_inicio < clinica.horario_abertura or
                horario_fim > clinica.horario_fechamento):
            self.__tela_atendimento.mostra_mensagem(
                "O atendimento deve ocorrer dentro do horário de funcionamento da clínica."
            )
            return None

        return data, horario_inicio, horario_fim

    def vincular_procedimento(self, procedimento):
        atendimento = self.__tela_atendimento.seleciona_atendimento(
            self.__atendimentos
        )

        if atendimento is None:
            self.__tela_atendimento.mostra_mensagem(
                "Atendimento não encontrado."
            )
            return False

        valor_anterior = atendimento.valor

        atendimento.procedimentos.append(procedimento)

        valor_procedimentos = 0

        for procedimento_atual in atendimento.procedimentos:
            valor_procedimentos += procedimento_atual.custo

        atendimento.valor_procedimentos = valor_procedimentos
        atendimento.valor = (
            atendimento.valor_atendimento + valor_procedimentos
        )

        self.__controlador_pagamentos.atualizar_valor_pagamento(
            atendimento, valor_anterior
        )

        return True
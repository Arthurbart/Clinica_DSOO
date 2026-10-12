from Views.telaRelatorio import TelaRelatorio


class ControladorRelatorio():

    def __init__(self, controlador_registro):
        self.__tela_relatorio = TelaRelatorio()
        self.__controlador_registro = controlador_registro

    def abre_tela(self):
        continua = True

        while continua:
            opcao = self.__tela_relatorio.mostrar_opcoes()

            if opcao == 1:
                self.relatorio_clinicas()
            elif opcao == 2:
                self.relatorio_atendimentos()
            elif opcao == 3:
                self.relatorio_procedimentos_populares()
            elif opcao == 4:
                self.relatorio_procedimentos_valor()
            elif opcao == 5:
                continua = False
            else:
                self.__tela_relatorio.mostra_mensagem("Opção inválida.")

    def relatorio_clinicas(self):
        atendimentos = self.__controlador_registro.obter_atendimentos()

        if not atendimentos:
            self.__tela_relatorio.mostra_mensagem(
                "Nenhum atendimento cadastrado."
            )
            return

        contagem = {}

        for atendimento in atendimentos:
            clinica = atendimento.clinica

            if clinica in contagem:
                contagem[clinica] += 1
            else:
                contagem[clinica] = 1

        self.__tela_relatorio.mostra_mensagem(
            "\n===== 3 CLÍNICAS COM MAIS ATENDIMENTOS ====="
        )

        quantidade_resultados = 0

        while contagem and quantidade_resultados < 3:
            maior_clinica = None
            maior_quantidade = 0

            for clinica in contagem:
                if contagem[clinica] > maior_quantidade:
                    maior_clinica = clinica
                    maior_quantidade = contagem[clinica]

            quantidade_resultados += 1

            self.__tela_relatorio.mostra_mensagem(
                f"{quantidade_resultados}º - {maior_clinica.nome} - "
                f"{maior_quantidade} atendimentos"
            )

            del contagem[maior_clinica]

    def relatorio_atendimentos(self):
        atendimentos = self.__controlador_registro.obter_atendimentos()

        if not atendimentos:
            self.__tela_relatorio.mostra_mensagem(
                "Nenhum atendimento cadastrado."
            )
            return

        mais_caros = atendimentos.copy()
        mais_baratos = atendimentos.copy()

        self.__tela_relatorio.mostra_mensagem(
            "\n===== 3 ATENDIMENTOS MAIS CAROS ====="
        )

        quantidade_resultados = 0

        while mais_caros and quantidade_resultados < 3:
            maior = mais_caros[0]

            for atendimento in mais_caros:
                if atendimento.valor > maior.valor:
                    maior = atendimento

            quantidade_resultados += 1

            self.__tela_relatorio.mostra_mensagem(
                f"{quantidade_resultados}º - "
                f"Paciente: {maior.paciente.nome} | "
                f"Clínica: {maior.clinica.nome} | "
                f"Valor: R$ {maior.valor:.2f}"
            )

            mais_caros.remove(maior)

        self.__tela_relatorio.mostra_mensagem(
            "\n===== 3 ATENDIMENTOS MAIS BARATOS ====="
        )

        quantidade_resultados = 0

        while mais_baratos and quantidade_resultados < 3:
            menor = mais_baratos[0]

            for atendimento in mais_baratos:
                if atendimento.valor < menor.valor:
                    menor = atendimento

            quantidade_resultados += 1

            self.__tela_relatorio.mostra_mensagem(
                f"{quantidade_resultados}º - "
                f"Paciente: {menor.paciente.nome} | "
                f"Clínica: {menor.clinica.nome} | "
                f"Valor: R$ {menor.valor:.2f}"
            )

            mais_baratos.remove(menor)

    def relatorio_procedimentos_populares(self):
        atendimentos = self.__controlador_registro.obter_atendimentos()

        if not atendimentos:
            self.__tela_relatorio.mostra_mensagem(
                "Nenhum atendimento cadastrado."
            )
            return

        contagem = {}

        for atendimento in atendimentos:
            for procedimento in atendimento.procedimentos:

                if procedimento.descricao in contagem:
                    contagem[procedimento.descricao] += 1
                else:
                    contagem[procedimento.descricao] = 1

        if not contagem:
            self.__tela_relatorio.mostra_mensagem(
                "Nenhum procedimento cadastrado."
            )
            return

        self.__tela_relatorio.mostra_mensagem(
            "\n===== 3 PROCEDIMENTOS MAIS REALIZADOS ====="
        )

        quantidade_resultados = 0

        while contagem and quantidade_resultados < 3:
            procedimento_mais_realizado = None
            maior_quantidade = 0

            for descricao in contagem:
                if contagem[descricao] > maior_quantidade:
                    procedimento_mais_realizado = descricao
                    maior_quantidade = contagem[descricao]

            quantidade_resultados += 1

            self.__tela_relatorio.mostra_mensagem(
                f"{quantidade_resultados}º - "
                f"{procedimento_mais_realizado} - "
                f"{maior_quantidade} realizações"
            )

            del contagem[procedimento_mais_realizado]

    def relatorio_procedimentos_valor(self):
        atendimentos = self.__controlador_registro.obter_atendimentos()

        if not atendimentos:
            self.__tela_relatorio.mostra_mensagem(
                "Nenhum atendimento cadastrado."
            )
            return

        procedimentos = []

        for atendimento in atendimentos:
            for procedimento in atendimento.procedimentos:
                procedimentos.append(procedimento)

        if not procedimentos:
            self.__tela_relatorio.mostra_mensagem(
                "Nenhum procedimento cadastrado."
            )
            return

        mais_caros = procedimentos.copy()
        mais_baratos = procedimentos.copy()

        self.__tela_relatorio.mostra_mensagem(
            "\n===== 3 PROCEDIMENTOS MAIS CAROS ====="
        )

        quantidade_resultados = 0

        while mais_caros and quantidade_resultados < 3:
            maior = mais_caros[0]

            for procedimento in mais_caros:
                if procedimento.custo > maior.custo:
                    maior = procedimento

            quantidade_resultados += 1

            self.__tela_relatorio.mostra_mensagem(
                f"{quantidade_resultados}º - "
                f"{maior.descricao} - "
                f"R$ {maior.custo:.2f}"
            )

            mais_caros.remove(maior)

        self.__tela_relatorio.mostra_mensagem(
            "\n===== 3 PROCEDIMENTOS MAIS BARATOS ====="
        )

        quantidade_resultados = 0

        while mais_baratos and quantidade_resultados < 3:
            menor = mais_baratos[0]

            for procedimento in mais_baratos:
                if procedimento.custo < menor.custo:
                    menor = procedimento

            quantidade_resultados += 1

            self.__tela_relatorio.mostra_mensagem(
                f"{quantidade_resultados}º - "
                f"{menor.descricao} - "
                f"R$ {menor.custo:.2f}"
            )

            mais_baratos.remove(menor)
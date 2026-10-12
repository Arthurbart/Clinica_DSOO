from Models.procedimento import Procedimento
from Views.telaProcedimento import TelaProcedimento

class ControladorProcedimento():
    def __init__(self, controlador_profissional):
        self.__tela_procedimento = TelaProcedimento()
        self.__procedimentos = []
        self.__controlador_profissional = controlador_profissional
        self.__controlador_atendimento = None

    def abre_tela(self):
        continua = True
        while continua:
            opcao = self.__tela_procedimento.mostrar_opcoes()

            if opcao == 1:
                self.cadastrar_procedimento()
            elif opcao == 2:
                self.listar_procedimentos()
            elif opcao == 3:
                self.editar_procedimento()
            elif opcao == 4:
                self.excluir_procedimento()
            elif opcao == 5:
                continua = False

    def obter_procedimentos(self):
        return self.__procedimentos

    def cadastrar_procedimento_por_atendimento(self):
        dados_procedimento = (
            self.__tela_procedimento.pega_dados_procedimento()
        )

        if dados_procedimento is None:
            return None

        profissional = (
            self.__controlador_profissional.encontrar_profissional_por_cpf(
                dados_procedimento["profissional"]
            )
        )

        if profissional is None:
            self.__tela_procedimento.mostra_mensagem(
                "Profissional não encontrado."
            )
            return None

        try:
            custo = float(dados_procedimento["custo"])

            if custo < 0:
                self.__tela_procedimento.mostra_mensagem(
                    "O custo não pode ser negativo."
                )
                return None

            procedimento = Procedimento(
                dados_procedimento["descricao"],
                custo,
                profissional
            )

            self.__procedimentos.append(procedimento)

            self.__tela_procedimento.mostra_mensagem(
                "Procedimento cadastrado com sucesso!"
            )

            return procedimento

        except ValueError:
            self.__tela_procedimento.mostra_mensagem(
                "Custo inválido! Digite um valor numérico."
            )
            return None

    def cadastrar_procedimento(self):
        atendimentos = self.__controlador_atendimento.obter_atendimentos()

        if not atendimentos:
            self.__tela_procedimento.mostra_mensagem(
                "Cadastre um atendimento antes de cadastrar um procedimento."
            )
            return None

        dados_procedimento = (
            self.__tela_procedimento.pega_dados_procedimento()
        )

        if dados_procedimento is None:
            return None

        profissional = (
            self.__controlador_profissional.encontrar_profissional_por_cpf(
                dados_procedimento["profissional"]
            )
        )

        if profissional is None:
            self.__tela_procedimento.mostra_mensagem(
                "Profissional não encontrado."
            )
            return None

        try:
            custo = float(dados_procedimento["custo"])

            if custo < 0:
                self.__tela_procedimento.mostra_mensagem(
                    "O custo não pode ser negativo."
                )
                return None

            procedimento = Procedimento(
                dados_procedimento["descricao"],
                custo,
                profissional
            )

            vinculado = (
                self.__controlador_atendimento.vincular_procedimento(
                    procedimento
                )
            )

            if not vinculado:
                return None

            self.__procedimentos.append(procedimento)

            self.__tela_procedimento.mostra_mensagem(
                "Procedimento cadastrado e vinculado com sucesso!"
            )

            return procedimento

        except ValueError:
            self.__tela_procedimento.mostra_mensagem(
                "Custo inválido! Digite um valor numérico."
            )
            return None

    def listar_procedimentos(self):
        if not self.__procedimentos:
            self.__tela_procedimento.mostra_mensagem("Nenhum procedimento cadastrado.")
            return
        for procedimento in self.__procedimentos:
            self.__tela_procedimento.mostra_mensagem(f"Descrição: {procedimento.descricao}, Custo: {procedimento.custo}, Profissional: {procedimento.profissional.nome}")

    def editar_procedimento(self):
        procedimento = self.__tela_procedimento.seleciona_procedimento(
            self.__procedimentos
        )

        if procedimento is None:
            self.__tela_procedimento.mostra_mensagem(
                "Procedimento não encontrado."
            )
            return

        novos_dados = self.__tela_procedimento.pega_dados_procedimento()

        if novos_dados is None:
            return None

        profissional = self.__controlador_profissional.encontrar_profissional_por_cpf(
            novos_dados["profissional"]
        )

        if profissional is None:
            self.__tela_procedimento.mostra_mensagem(
                "Profissional não encontrado."
            )
            return

        try:
            custo = float(novos_dados["custo"])

            if custo < 0:
                self.__tela_procedimento.mostra_mensagem(
                    "O custo não pode ser negativo."
                )
                return

            procedimento.descricao = novos_dados["descricao"]
            procedimento.custo = custo
            procedimento.profissional = profissional

            self.__controlador_atendimento.atualizar_procedimento(
                procedimento
            )

            self.__tela_procedimento.mostra_mensagem(
                "Procedimento editado com sucesso!"
            )

        except ValueError:
            self.__tela_procedimento.mostra_mensagem(
                "Custo inválido! Digite um valor numérico."
            )

    def excluir_procedimento(self):
        procedimento = self.__tela_procedimento.seleciona_procedimento(
            self.__procedimentos
        )

        if procedimento is None:
            self.__tela_procedimento.mostra_mensagem(
                "Procedimento não encontrado."
            )
            return

        self.__controlador_atendimento.remover_procedimento(
            procedimento
        )

        self.__procedimentos.remove(procedimento)

        self.__tela_procedimento.mostra_mensagem(
            "Procedimento excluído com sucesso!"
        )

    def definir_controlador_atendimento(self, controlador_atendimento):
        self.__controlador_atendimento = controlador_atendimento

    def excluir_procedimentos_por_atendimento(self, atendimento):
        for procedimento in atendimento.procedimentos[:]:
            if procedimento in self.__procedimentos:
                self.__procedimentos.remove(procedimento)

        atendimento.procedimentos = []
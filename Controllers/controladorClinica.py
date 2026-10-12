from Views.telaClinica import TelaClinica
from Models.clinica import Clinica
from Exceptions.clinicaDuplicadaException import ClinicaDuplicadaException
from datetime import datetime

class ControladorClinica:
    def __init__(self):
        self.__tela_clinica = TelaClinica()
        self.__clinicas = []

    def abre_tela(self):
        continua = True
        while continua:
            opcao = self.__tela_clinica.mostrar_opcoes()

            if opcao == 1:
                self.cadastrar_clinica()
            elif opcao == 2:
                self.listar_clinicas()
            elif opcao == 3:
                self.editar_clinica()
            elif opcao == 4:
                self.excluir_clinica()
            elif opcao == 5:
                continua = False

    def cadastrar_clinica(self):
        dados_clinica = self.__tela_clinica.pega_dados_clinica()
        try:
            self.verificar_nome_duplicado(dados_clinica["nome"])

            abertura, fechamento = self.validar_horarios(
                dados_clinica["horario_abertura"], dados_clinica["horario_fechamento"]
            )

            clinica = Clinica(dados_clinica["nome"], dados_clinica["localizacao"], dados_clinica["descricao"], abertura, fechamento)
            self.__clinicas.append(clinica)
            self.__tela_clinica.mostra_mensagem("Clínica cadastrada com sucesso!")
        except (ClinicaDuplicadaException, ValueError) as erro:
            self.__tela_clinica.mostra_mensagem(str(erro))

    def listar_clinicas(self):
        if not self.__clinicas:
            self.__tela_clinica.mostra_mensagem("Nenhuma clínica cadastrada.")
            return
        for clinica in self.__clinicas:
            self.__tela_clinica.mostra_mensagem(f"Nome: {clinica.nome}, Local: {clinica.localizacao}, Descrição: {clinica.descricao}, Horário de Abertura: {clinica.horario_abertura}, Horário de Fechamento: {clinica.horario_fechamento}")

    def editar_clinica(self):
        nome = self.__tela_clinica.seleciona_clinica_por_nome()
        clinica = self.encontrar_clinica_por_nome(nome)
        if clinica:
            novos_dados = self.__tela_clinica.pega_dados_clinica()
            try:
                self.verificar_nome_duplicado(novos_dados["nome"], clinica)

                abertura, fechamento = self.validar_horarios(
                    novos_dados["horario_abertura"], novos_dados["horario_fechamento"]
                )

                clinica.nome = novos_dados["nome"]
                clinica.localizacao = novos_dados["localizacao"]
                clinica.descricao = novos_dados["descricao"]
                clinica.horario_abertura = abertura
                clinica.horario_fechamento = fechamento
                self.__tela_clinica.mostra_mensagem("Clínica editada com sucesso!")
            except (ClinicaDuplicadaException, ValueError) as erro:
                self.__tela_clinica.mostra_mensagem(str(erro))
        else:
            self.__tela_clinica.mostra_mensagem("Clínica não encontrada.")

    def excluir_clinica(self):
        nome = self.__tela_clinica.seleciona_clinica_por_nome()
        clinica = self.encontrar_clinica_por_nome(nome)
        if clinica:
            self.__clinicas.remove(clinica)
            self.__tela_clinica.mostra_mensagem("Clínica excluída com sucesso!")
        else:
            self.__tela_clinica.mostra_mensagem("Clínica não encontrada.")

    def encontrar_clinica_por_nome(self, nome):
        for clinica in self.__clinicas:
            if clinica.nome == nome:
                return clinica
        return None

    def verificar_nome_duplicado(self, nome, clinica_atual=None):
        for clinica in self.__clinicas:
            if clinica.nome.strip().lower() == nome.strip().lower() and clinica != clinica_atual:
                raise ClinicaDuplicadaException()

    def validar_horarios(self, horario_abertura, horario_fechamento):
        try:
            abertura = datetime.strptime(
                horario_abertura, "%H:%M"
            ).time()

            fechamento = datetime.strptime(
                horario_fechamento, "%H:%M"
            ).time()

        except ValueError:
            raise ValueError(
                "Horário inválido! Utilize o formato HH:MM."
            )

        if abertura >= fechamento:
            raise ValueError(
                "O horário de abertura deve ser anterior ao fechamento."
            )

        return abertura, fechamento
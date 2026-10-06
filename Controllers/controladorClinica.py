from Views.telaClinica import TelaClinica
from Models.clinica import Clinica

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
        clinica = Clinica(dados_clinica["nome"], dados_clinica["localizacao"], dados_clinica["descricao"])
        self.__clinicas.append(clinica)
        self.__tela_clinica.mostra_mensagem("Clínica cadastrada com sucesso!")

    def listar_clinicas(self):
        if not self.__clinicas:
            self.__tela_clinica.mostra_mensagem("Nenhuma clínica cadastrada.")
            return
        for clinica in self.__clinicas:
            self.__tela_clinica.mostra_mensagem(f"Nome: {clinica.nome}, Local: {clinica.localizacao}, Descrição: {clinica.descricao}")

    def editar_clinica(self):
        nome = self.__tela_clinica.seleciona_clinica_por_nome()
        clinica = self.encontrar_clinica_por_nome(nome)
        if clinica:
            novos_dados = self.__tela_clinica.pega_dados_clinica()
            clinica.nome = novos_dados["nome"]
            clinica.localizacao = novos_dados["localizacao"]
            clinica.descricao = novos_dados["descricao"]
            self.__tela_clinica.mostra_mensagem("Clínica editada com sucesso!")
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

    
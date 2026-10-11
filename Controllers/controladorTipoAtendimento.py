from Views.telaTipoAtendimento import TelaTipoAtendimento
from Models.tipoAtendimento import TipoAtendimento

class ControladorTipoAtendimento:
    def __init__(self):
        self.__tela_tipo_atendimento = TelaTipoAtendimento()
        self.__tipos_atendimento = []

    def abre_tela(self):
        continua = True
        while continua:
            opcao = self.__tela_tipo_atendimento.mostrar_opcoes()

            if opcao == 1:
                self.cadastrar_tipo_atendimento()
            elif opcao == 2:
                self.listar_tipos_atendimento()
            elif opcao == 3:
                self.editar_tipo_atendimento()
            elif opcao == 4:
                self.excluir_tipo_atendimento()
            elif opcao == 5:
                continua = False

    def cadastrar_tipo_atendimento(self):
        dados_tipo_atendimento = self.__tela_tipo_atendimento.pega_dados_tipo_atendimento()
        tipo_atendimento = TipoAtendimento(dados_tipo_atendimento["nome"], dados_tipo_atendimento["descricao"])
        self.__tipos_atendimento.append(tipo_atendimento)
        self.__tela_tipo_atendimento.mostra_mensagem("Tipo de atendimento cadastrado com sucesso!")

    def listar_tipos_atendimento(self):
        if not self.__tipos_atendimento:
            self.__tela_tipo_atendimento.mostra_mensagem("Nenhum tipo de atendimento cadastrado.")
            return
        for tipo_atendimento in self.__tipos_atendimento:
            self.__tela_tipo_atendimento.mostra_mensagem(f"Nome: {tipo_atendimento.nome}, Descrição: {tipo_atendimento.descricao}")

    def editar_tipo_atendimento(self):
        nome = self.__tela_tipo_atendimento.seleciona_tipo_atendimento_por_nome()
        tipo_atendimento = self.encontrar_tipo_atendimento_por_nome(nome)
        if tipo_atendimento:
            novos_dados = self.__tela_tipo_atendimento.pega_dados_tipo_atendimento()
            tipo_atendimento.nome = novos_dados["nome"]
            tipo_atendimento.descricao = novos_dados["descricao"]
            self.__tela_tipo_atendimento.mostra_mensagem("Tipo de atendimento editado com sucesso!")
        else:
            self.__tela_tipo_atendimento.mostra_mensagem("Tipo de atendimento não encontrado.")

    def excluir_tipo_atendimento(self):
        nome = self.__tela_tipo_atendimento.seleciona_tipo_atendimento_por_nome()
        tipo_atendimento = self.encontrar_tipo_atendimento_por_nome(nome)
        if tipo_atendimento:
            self.__tipos_atendimento.remove(tipo_atendimento)
            self.__tela_tipo_atendimento.mostra_mensagem("Tipo de atendimento excluído com sucesso!")
        else:
            self.__tela_tipo_atendimento.mostra_mensagem("Tipo de atendimento não encontrado.")

    def encontrar_tipo_atendimento_por_nome(self, nome):
        for tipo_atendimento in self.__tipos_atendimento:
            if tipo_atendimento.nome == nome:
                return tipo_atendimento
        return None

    
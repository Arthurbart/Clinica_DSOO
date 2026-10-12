from Views.telaProfissional import TelaProfissional
from Models.profissional import Profissional
from Exceptions.cpfDuplicadoException import CpfDuplicadoException
class ControladorProfissional:
    def __init__(self, controlador_pessoa):
        self.__tela_profissional = TelaProfissional()
        self.__profissionais = []
        self.__controlador_pessoa = controlador_pessoa

    def abre_tela(self):
        continua = True
        while continua:
            opcao = self.__tela_profissional.mostrar_opcoes()

            if opcao == 1:
                self.cadastrar_profissional()
            elif opcao == 2:
                self.listar_profissionais()
            elif opcao == 3:
                self.editar_profissional()
            elif opcao == 4:
                self.excluir_profissional()
            elif opcao == 5:
                continua = False

    def cadastrar_profissional(self):
        dados_profissional = self.__tela_profissional.pega_dados_profissional()

        try:
            self.__controlador_pessoa.verificar_cpf_duplicado(dados_profissional["cpf"])

            profissional = Profissional(
                dados_profissional["nome"],
                dados_profissional["celular"],
                dados_profissional["cpf"],
                dados_profissional["especialidade"],
                dados_profissional["registro_profissional"]
            )

            self.__profissionais.append(profissional)
            self.__tela_profissional.mostra_mensagem(
                "Profissional cadastrado com sucesso!"
            )

        except CpfDuplicadoException as erro:
            self.__tela_profissional.mostra_mensagem(str(erro))

    def listar_profissionais(self):
        if not self.__profissionais:
            self.__tela_profissional.mostra_mensagem("Nenhum profissional cadastrado.")
            return
        for profissional in self.__profissionais:
            self.__tela_profissional.mostra_mensagem(f"Nome: {profissional.nome}, Celular: {profissional.celular}, CPF: {profissional.cpf}, Especialidade: {profissional.especialidade}, Registro: {profissional.registro_profissional}")

    def editar_profissional(self):
        cpf = self.__tela_profissional.seleciona_profissional_por_cpf()
        profissional = self.encontrar_profissional_por_cpf(cpf)
        if profissional:
            novos_dados = self.__tela_profissional.pega_dados_profissional()
            try:
                self.__controlador_pessoa.verificar_cpf_duplicado(novos_dados["cpf"], profissional)

                profissional.nome = novos_dados["nome"]
                profissional.celular = novos_dados["celular"]
                profissional.cpf = novos_dados["cpf"]
                profissional.especialidade = novos_dados["especialidade"]
                profissional.registro_profissional = novos_dados["registro_profissional"]

                self.__tela_profissional.mostra_mensagem("Profissional editado com sucesso!")
            except CpfDuplicadoException as erro:
                self.__tela_profissional.mostra_mensagem(str(erro))
        else:
            self.__tela_profissional.mostra_mensagem("Profissional não encontrado.")

    def excluir_profissional(self):
        cpf = self.__tela_profissional.seleciona_profissional_por_cpf()
        profissional = self.encontrar_profissional_por_cpf(cpf)
        if profissional:
            self.__profissionais.remove(profissional)
            self.__tela_profissional.mostra_mensagem("Profissional excluído com sucesso!")
        else:
            self.__tela_profissional.mostra_mensagem("Profissional não encontrado.")

    def encontrar_profissional_por_cpf(self, cpf):
        for profissional in self.__profissionais:
            if profissional.cpf == cpf:
                return profissional
        return None

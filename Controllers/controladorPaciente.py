from Views.telaPaciente import TelaPaciente
from Models.paciente import Paciente
from Exceptions.cpfDuplicadoException import CpfDuplicadoException
from Exceptions.menorDeIdadeException import MenorDeIdadeException
class ControladorPaciente:
    def __init__(self, controlador_pessoa):
        self.__tela_paciente = TelaPaciente()
        self.__pacientes = []
        self.__controlador_pessoa = controlador_pessoa

    def abre_tela(self):
        continua = True
        while continua:
            opcao = self.__tela_paciente.mostrar_opcoes()

            if opcao == 1:
                self.cadastrar_paciente()
            elif opcao == 2:
                self.listar_pacientes()
            elif opcao == 3:
                self.editar_paciente()
            elif opcao == 4:
                self.excluir_paciente()
            elif opcao == 5:
                continua = False

    def cadastrar_paciente(self):
        dados_paciente = self.__tela_paciente.pega_dados_paciente()

        try:
            if int(dados_paciente["idade"]) < 18:
                raise MenorDeIdadeException()

            self.__controlador_pessoa.verificar_cpf_duplicado(dados_paciente["cpf"])

            paciente = Paciente(
                dados_paciente["nome"],
                dados_paciente["celular"],
                dados_paciente["cpf"],
                dados_paciente["idade"]
            )

            self.__pacientes.append(paciente)
            self.__tela_paciente.mostra_mensagem("Paciente cadastrado com sucesso!")

        except (CpfDuplicadoException, MenorDeIdadeException) as erro:
            self.__tela_paciente.mostra_mensagem(str(erro))

    def listar_pacientes(self):
        if not self.__pacientes:
            self.__tela_paciente.mostra_mensagem("Nenhum paciente cadastrado.")
            return
        for paciente in self.__pacientes:
            self.__tela_paciente.mostra_mensagem(f"Nome: {paciente.nome}, Celular: {paciente.celular}, CPF: {paciente.cpf}, Idade: {paciente.idade}")

    def editar_paciente(self):
        cpf = self.__tela_paciente.seleciona_paciente_por_cpf()
        paciente = self.encontrar_paciente_por_cpf(cpf)

        if paciente:
            novos_dados = self.__tela_paciente.pega_dados_paciente()

            try:
                if int(novos_dados["idade"]) < 18:
                    raise MenorDeIdadeException()

                self.__controlador_pessoa.verificar_cpf_duplicado(novos_dados["cpf"], paciente)

                paciente.nome = novos_dados["nome"]
                paciente.celular = novos_dados["celular"]
                paciente.cpf = novos_dados["cpf"]
                paciente.idade = novos_dados["idade"]

                self.__tela_paciente.mostra_mensagem("Paciente editado com sucesso!")

            except (CpfDuplicadoException, MenorDeIdadeException) as erro:
                self.__tela_paciente.mostra_mensagem(str(erro))

        else:
            self.__tela_paciente.mostra_mensagem("Paciente não encontrado.")

    def excluir_paciente(self):
        cpf = self.__tela_paciente.seleciona_paciente_por_cpf()
        paciente = self.encontrar_paciente_por_cpf(cpf)
        if paciente:
            self.__pacientes.remove(paciente)
            self.__tela_paciente.mostra_mensagem("Paciente excluído com sucesso!")
        else:
            self.__tela_paciente.mostra_mensagem("Paciente não encontrado.")

    def encontrar_paciente_por_cpf(self, cpf):
        for paciente in self.__pacientes:
            if paciente.cpf == cpf:
                return paciente
        return None

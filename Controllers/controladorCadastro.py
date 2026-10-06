from Views.telaCadastro import TelaCadastro
from Controllers import controladorClinica, controladorPaciente, controladorProfissional, controladorTipoAtendimento


class ControladorCadastro():

    def __init__(self, controlador_tipo_atendimento, controlador_paciente, controlador_profissional, controlador_clinica):
        self.__tela_cadastro = TelaCadastro()
        self.__controlador_clinica = controlador_clinica
        self.__controlador_paciente = controlador_paciente
        self.__controlador_profissional = controlador_profissional
        self.__controlador_tipo_atendimento = controlador_tipo_atendimento

    def abre_tela(self):
        continua = True

        while continua:

            opcao = self.__tela_cadastro.mostrar_opcoes()

            if opcao == 1:
                self.__controlador_paciente.abre_tela()

            elif opcao == 2:
                self.__controlador_profissional.abre_tela()

            elif opcao == 3:
                self.__controlador_clinica.abre_tela()

            elif opcao == 4:
                self.__controlador_tipo_atendimento.abre_tela()

            elif opcao == 5:
                continua = False

            else:
                print("Opção inválida.")
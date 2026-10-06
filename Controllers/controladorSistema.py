from Controllers import controladorCadastro
from Controllers import controladorRegistro
from Controllers import controladorRelatorio
from Controllers import controladorTipoAtendimento
from Controllers import controladorPaciente
from Controllers import controladorProfissional
from Controllers import controladorClinica

from Views.telaSistema import TelaSistema


class ControladorSistema():

    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_tipo_atendimento = (controladorTipoAtendimento.ControladorTipoAtendimento())
        self.__controlador_paciente = controladorPaciente.ControladorPaciente()
        self.__controlador_profissional = controladorProfissional.ControladorProfissional()
        self.__controlador_clinica = controladorClinica.ControladorClinica()
        self.__controladorCadastro = controladorCadastro.ControladorCadastro(self.__controlador_tipo_atendimento, self.__controlador_paciente, self.__controlador_profissional, self.__controlador_clinica)
        self.__controladorRegistro = controladorRegistro.ControladorRegistro(self.__controlador_tipo_atendimento, self.__controlador_paciente, self.__controlador_profissional, self.__controlador_clinica)
        self.__controladorRelatorio = controladorRelatorio.ControladorRelatorio(self.__controladorRegistro)


    def inicializa_sistema(self):
        self.abre_tela()

    def abre_tela(self):
        continua = True

        while continua:
            opcao = self.__tela_sistema.mostrar_opcoes()

            if opcao == 1:
                self.__controladorCadastro.abre_tela()

            elif opcao == 2:
                self.__controladorRegistro.abre_tela()

            elif opcao == 3:
                self.__controladorRelatorio.abre_tela()

            elif opcao == 4:
                continua = False

            else:
                print("Opção inválida.")

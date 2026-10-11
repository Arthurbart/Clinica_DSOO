from Views.telaRegistro import TelaRegistro
from Controllers import controladorAtendimento, controladorProcedimento, controladorPagamento, controladorTipoAtendimento

class ControladorRegistro():

    def __init__(self, controlador_tipo_atendimento, controlador_paciente, controlador_profissional, controlador_clinica):
        self.__tela_registro = TelaRegistro()
        self.__controlador_profissional = controlador_profissional
        self.__controlador_procedimentos = controladorProcedimento.ControladorProcedimento(self.__controlador_profissional)
        self.__controlador_tipo_atendimento = controlador_tipo_atendimento
        self.__controlador_pagamentos = controladorPagamento.ControladorPagamento()
        self.__controlador_paciente = controlador_paciente
        self.__controlador_clinica = controlador_clinica
        self.__controlador_atendimentos = controladorAtendimento.ControladorAtendimento(
            self.__controlador_procedimentos,
            self.__controlador_tipo_atendimento,
            self.__controlador_paciente,
            self.__controlador_profissional,
            self.__controlador_clinica,
            self.__controlador_pagamentos
        )

    
    def abre_tela(self):
        continua = True

        while continua:

            opcao = self.__tela_registro.mostrar_opcoes()

            if opcao == 1:
                self.__controlador_atendimentos.abre_tela()

            elif opcao == 2:
                self.__controlador_procedimentos.abre_tela()

            elif opcao == 3:
                self.__controlador_pagamentos.abre_tela()

            elif opcao == 4:
                continua = False

            else:
                print("Opção inválida.")


    def obter_atendimentos(self):
        return self.__controlador_atendimentos.obter_atendimentos()

    def obter_procedimentos(self):
        return self.__controlador_procedimentos.obter_procedimentos()
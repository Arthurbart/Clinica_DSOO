from Exceptions.cpfDuplicadoException import CpfDuplicadoException


class ControladorPessoa:
    def __init__(self):
        self.__controlador_paciente = None
        self.__controlador_profissional = None

    def adicionar_controladores(
        self, controlador_paciente, controlador_profissional
    ):
        self.__controlador_paciente = controlador_paciente
        self.__controlador_profissional = controlador_profissional

    def verificar_cpf_duplicado(self, cpf, pessoa_atual=None):
        paciente = (
            self.__controlador_paciente
            .encontrar_paciente_por_cpf(cpf)
        )

        profissional = (
            self.__controlador_profissional
            .encontrar_profissional_por_cpf(cpf)
        )

        if paciente is not None and paciente != pessoa_atual:
            raise CpfDuplicadoException()

        if profissional is not None and profissional != pessoa_atual:
            raise CpfDuplicadoException()

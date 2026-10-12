class Atendimento():
    def __init__(self, clinica, paciente, profissional, data,
                 horario_inicio, horario_fim, tipo_atendimento,
                 valor_atendimento, valor_procedimentos, valor,
                 procedimentos):

        self.__clinica = clinica
        self.__paciente = paciente
        self.__profissional = profissional
        self.__data = data
        self.__horario_inicio = horario_inicio
        self.__horario_fim = horario_fim
        self.__tipo_atendimento = tipo_atendimento
        self.__valor_atendimento = valor_atendimento
        self.__valor_procedimentos = valor_procedimentos
        self.__valor = valor
        self.__procedimentos = procedimentos

    @property
    def clinica(self):
        return self.__clinica

    @clinica.setter
    def clinica(self, clinica):
        self.__clinica = clinica

    @property
    def paciente(self):
        return self.__paciente

    @paciente.setter
    def paciente(self, paciente):
        self.__paciente = paciente

    @property
    def profissional(self):
        return self.__profissional

    @profissional.setter
    def profissional(self, profissional):
        self.__profissional = profissional

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def horario_inicio(self):
        return self.__horario_inicio

    @horario_inicio.setter
    def horario_inicio(self, horario_inicio):
        self.__horario_inicio = horario_inicio

    @property
    def horario_fim(self):
        return self.__horario_fim

    @horario_fim.setter
    def horario_fim(self, horario_fim):
        self.__horario_fim = horario_fim

    @property
    def tipo_atendimento(self):
        return self.__tipo_atendimento

    @tipo_atendimento.setter
    def tipo_atendimento(self, tipo_atendimento):
        self.__tipo_atendimento = tipo_atendimento

    @property
    def valor_atendimento(self):
        return self.__valor_atendimento

    @valor_atendimento.setter
    def valor_atendimento(self, valor_atendimento):
        self.__valor_atendimento = valor_atendimento

    @property
    def valor_procedimentos(self):
        return self.__valor_procedimentos

    @valor_procedimentos.setter
    def valor_procedimentos(self, valor_procedimentos):
        self.__valor_procedimentos = valor_procedimentos

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        self.__valor = valor

    @property
    def procedimentos(self):
        return self.__procedimentos

    @procedimentos.setter
    def procedimentos(self, procedimentos):
        self.__procedimentos = procedimentos
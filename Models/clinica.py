class Clinica():
    def __init__(self, nome, localizacao, descricao, horario_abertura, horario_fechamento):
        self.__nome = nome
        self.__localizacao = localizacao
        self.__descricao = descricao
        self.__horario_abertura = horario_abertura
        self.__horario_fechamento = horario_fechamento

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def localizacao(self):
        return self.__localizacao

    @localizacao.setter
    def localizacao(self, localizacao):
        self.__localizacao = localizacao

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def horario_abertura(self):
        return self.__horario_abertura

    @horario_abertura.setter
    def horario_abertura(self, horario_abertura):
        self.__horario_abertura = horario_abertura

    @property
    def horario_fechamento(self):
        return self.__horario_fechamento

    @horario_fechamento.setter
    def horario_fechamento(self, horario_fechamento):
        self.__horario_fechamento = horario_fechamento
class Clinica():
    def __init__(self, nome, localizacao, descricao):
        self.__nome = nome
        self.__localizacao = localizacao
        self.__descricao = descricao

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

    
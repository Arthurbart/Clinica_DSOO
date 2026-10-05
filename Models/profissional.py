from Models.pessoa import Pessoa


class Profissional(Pessoa):
    def __init__(self, nome, celular, cpf, especialidade, registro_profissional):
        super().__init__(nome, celular, cpf)
        self.__especialidade = especialidade
        self.__registro_profissional = registro_profissional

    @property
    def especialidade(self):
        return self.__especialidade

    @especialidade.setter
    def especialidade(self, especialidade):
        self.__especialidade = especialidade

    @property
    def registro_profissional(self):
        return self.__registro_profissional

    @registro_profissional.setter
    def registro_profissional(self, registro_profissional):
        self.__registro_profissional = registro_profissional
from Models.pessoa import Pessoa

class Paciente(Pessoa):
    def __init__(self, nome, celular, cpf, idade):
        super().__init__(nome, celular, cpf)
        self.__idade = idade

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        self.__idade = idade
from Models.pagamento import Pagamento

class PagamentoCartao(Pagamento):
    def __init__(self, data, atendimento, paciente, valor_pago,
                 numero_cartao, bandeira):
        super().__init__(data, atendimento, paciente, valor_pago)
        self.__numero_cartao = numero_cartao
        self.__bandeira = bandeira

    @property
    def numero_cartao(self):
        return self.__numero_cartao

    @numero_cartao.setter
    def numero_cartao(self, numero_cartao):
        self.__numero_cartao = numero_cartao

    @property
    def bandeira(self):
        return self.__bandeira

    @bandeira.setter
    def bandeira(self, bandeira):
        self.__bandeira = bandeira

    def realizar_pagamento(self):
        pass
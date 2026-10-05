from Models.pagamento import Pagamento


class PagamentoDinheiro(Pagamento):
    def __init__(self, data, atendimento, paciente, valor_pago):
        super().__init__(data, atendimento, paciente, valor_pago)

from Models.pagamento import Pagamento

class PagamentoPix(Pagamento):
    def __init__(self, data, atendimento, paciente, valor_pago, cpf_pagador):
        super().__init__(data, atendimento, paciente, valor_pago)
        self.__cpf_pagador = cpf_pagador

    @property
    def cpf_pagador(self):
        return self.__cpf_pagador

    @cpf_pagador.setter
    def cpf_pagador(self, cpf_pagador):
        self.__cpf_pagador = cpf_pagador


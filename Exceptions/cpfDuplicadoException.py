class CpfDuplicadoException(Exception):
    def __init__(self):
        super().__init__("Já existe uma pessoa cadastrada com esse CPF.")
class MenorDeIdadeException(Exception):
    def __init__(self):
        super().__init__("O paciente deve ter pelo menos 18 anos.")
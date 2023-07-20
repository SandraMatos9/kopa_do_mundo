# NegativeTitlesError: cuja mensagem deverá ser "titles cannot be negative".
class NegativeTitlesError(Exception):
    def __init__(self, message):
        self.message = message


# InvalidYearCupError: que deverá ter a mensagem "there was no world cup this year".
class InvalidYearCupError(Exception):
    def __init__(self, message):
        self.message = message


# ImpossibleTitlesError: onde a mensagem deve ser "impossible to have more titles than disputed cups"
class ImpossibleTitlesError(Exception):
    def __init__(self, message):
        self.message = message

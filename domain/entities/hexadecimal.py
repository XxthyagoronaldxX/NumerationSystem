from domain.constants.hexadecimal import HEXADECIMAL
from domain.errors.hexadecimal_is_not_legit import HexadecimalIsNotLegit


class HexadecimalEntity:
    def __init__(self, hexadecimal):
        self._hexadecimal = hexadecimal

    @staticmethod
    def __hexadecimalIsLegit(hexadecimal):
        for i in hexadecimal:
            if not HEXADECIMAL.__contains__(i):
                return False

        return True

    @staticmethod
    def createEntity(hexadecimal: int):
        if not HexadecimalEntity.__hexadecimalIsLegit(hexadecimal):
            return HexadecimalIsNotLegit()

        return HexadecimalEntity(hexadecimal)

    def getHexadecimal(self):
        return self._hexadecimal

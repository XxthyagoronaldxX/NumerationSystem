from domain.errors.octal_is_not_legit import OctalIsNotLegitError


class OctalEntity:
    def __init__(self, octal):
        self._octal = octal

    @staticmethod
    def __octalIsLegit(octal):
        for i in octal:
            if int(i) < 0 or int(i) > 7:
                return False

        return True

    @staticmethod
    def createEntity(octal):
        if not OctalEntity.__octalIsLegit(octal):
            return OctalIsNotLegitError()

        return OctalEntity(octal)
    
    def getOctal(self):
        return self._octal

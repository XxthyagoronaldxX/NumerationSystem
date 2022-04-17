class HexadecimalIsNotLegitError(Exception):
    def __init__(self, message='HexadecimalIsNotLegit'):
        super().__init__(message)

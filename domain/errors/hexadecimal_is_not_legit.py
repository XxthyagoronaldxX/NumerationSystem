class HexadecimalIsNotLegitError(Exception):
    def __init__(self):
        super().__init__('HexadecimalIsNotLegit')

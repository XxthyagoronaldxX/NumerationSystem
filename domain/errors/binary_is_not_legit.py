class BinaryIsNotLegitError(Exception):
    def __init__(self, message='BinaryIsNotLegitError'):
        super().__init__(message)

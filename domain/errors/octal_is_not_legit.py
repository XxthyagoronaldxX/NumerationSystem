class OctalIsNotLegitError(Exception):
    def __init__(self, message='OctalIsNotLegit'):
        super().__init__(message)

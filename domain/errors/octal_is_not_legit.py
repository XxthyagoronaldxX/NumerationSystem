class OctalIsNotLegitError(Exception):
    def __init__(self):
        super().__init__('OctalIsNotLegit')

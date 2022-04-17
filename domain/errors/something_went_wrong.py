class SomethingWentWrong(Exception):
    def __init__(self, message="SomethingWentWrong"):
        super().__init__(message)
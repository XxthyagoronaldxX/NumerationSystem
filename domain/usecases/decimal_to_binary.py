from abc import abstractmethod
from math import floor
from domain.entities.binary import BinaryEntity
from domain.entities.decimal import DecimalEntity


class DecimalToBinaryUsecase:
    @abstractmethod
    def call(self, decimalEntity: DecimalEntity, bold: int = 0):
        pass


class ImplDecimalToBinaryUsecase(DecimalToBinaryUsecase):
    def call(self, decimalEntity: DecimalEntity, bold: int = 0):
        decimal = decimalEntity.getDecimal()
        binary = ''

        while decimal > 0:
            if decimal % 2 != 0:
                binary = '1' + binary
            else:
                binary = '0' + binary

            decimal = floor(decimal/2)
        
        if bold != 0 and bold > binary.__len__():
            binary = ((bold - (binary.__len__()))*'0') + binary

        return BinaryEntity.createEntity(binary)

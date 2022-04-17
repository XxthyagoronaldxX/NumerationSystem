from abc import ABC, abstractmethod
from math import floor
from domain.entities.binary import BinaryEntity
from domain.entities.decimal import DecimalEntity
from domain.errors.something_went_wrong import SomethingWentWrong


class DecimalToBinaryUsecase(ABC):
    @abstractmethod
    def call(self, decimal: int, bold: int = 0):
        pass


class ImplDecimalToBinaryUsecase(DecimalToBinaryUsecase):
    def call(self, decimal: int, fill: int = 0):
        try:
            decimalEntity = DecimalEntity.createEntity(decimal)

            return self._convertingDecimalToBinary(decimalEntity, fill)
        except:
            return SomethingWentWrong()
    
    def _convertingDecimalToBinary(self, decimalEntity: DecimalEntity, fill: int):
        decimal = decimalEntity.getDecimal()
        binary = ''

        while decimal > 0:
            if decimal % 2 != 0:
                binary = '1' + binary
            else:
                binary = '0' + binary

            decimal = floor(decimal/2)
        
        if fill != 0 and fill > binary.__len__():
            binary = ((fill - (binary.__len__()))*'0') + binary

        return BinaryEntity.createEntity(binary)

from abc import abstractmethod
from math import floor
from domain.entities.binary import BinaryEntity
from domain.entities.decimal import DecimalEntity


class DecimalToBinaryUsecase:
    @abstractmethod
    def call(self, decimal):
        pass


class ImplDecimalToBinaryUsecase(DecimalToBinaryUsecase):
    def call(self, decimalEntity: DecimalEntity):
        decimal = decimalEntity.getDecimal()
        binary = ''

        while decimal > 0:
            if decimal % 2 != 0:
                binary += '1'
            else:
                binary += '0'

            decimal = floor(decimal/2)

        return BinaryEntity.createEntity(''.join(reversed(binary)))

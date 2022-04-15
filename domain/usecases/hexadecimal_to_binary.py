from abc import abstractmethod
from unicodedata import decimal
from domain.constants.hexadecimal import HEXADECIMAL
from domain.entities.binary import BinaryEntity
from domain.entities.decimal import DecimalEntity

from domain.entities.hexadecimal import HexadecimalEntity
from domain.usecases.decimal_to_binary import DecimalToBinaryUsecase

class HexadecimalToBinary:
    @abstractmethod
    def call(self, hexadecimalEntity: HexadecimalEntity):
        pass

class ImplHexadecimalToBinary(HexadecimalToBinary):
    def __init__(self, decimalToBinaryUsecase: DecimalToBinaryUsecase):
        self._decimalToBinaryUsecase = decimalToBinaryUsecase

    def call(self, hexadecimalEntity: HexadecimalEntity):
        hexadecimal = hexadecimalEntity.getHexadecimal()

        hexadecimal_length = hexadecimal.__len__() - 1

        binary = ''

        for i in range(hexadecimal_length, -1, -1):
            decimal = HEXADECIMAL.index(hexadecimal[i])

            decimalEntity = DecimalEntity.createEntity(decimal)

            binaryEntity = self._decimalToBinaryUsecase.call(decimalEntity)

            binary = binaryEntity.getBinary() + binary
        
        return BinaryEntity.createEntity(binary)
            
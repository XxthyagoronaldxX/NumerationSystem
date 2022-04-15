from abc import abstractmethod
from unicodedata import decimal
from domain.constants.hexadecimal import HEXADECIMAL
from domain.entities.binary import BinaryEntity
from domain.entities.decimal import DecimalEntity

from domain.entities.hexadecimal import HexadecimalEntity
from domain.usecases.decimal_to_binary import DecimalToBinaryUsecase

class HexadecimalToBinaryUsecase:
    @abstractmethod
    def call(self, hexadecimalEntity: HexadecimalEntity):
        pass

class ImplHexadecimalToBinaryUsecase(HexadecimalToBinaryUsecase):
    def __init__(self, decimalToBinaryUsecase: DecimalToBinaryUsecase):
        self._decimalToBinaryUsecase = decimalToBinaryUsecase

    def call(self, hexadecimalEntity: HexadecimalEntity):
        hexadecimal = hexadecimalEntity.getHexadecimal()

        hexadecimal_length = hexadecimal.__len__() - 1

        binary = ''

        for i in range(hexadecimal_length, -1, -1):
            decimal = HEXADECIMAL.index(hexadecimal[i])

            decimalEntity = DecimalEntity.createEntity(decimal)

            binaryEntity = self._decimalToBinaryUsecase.call(decimalEntity, 4)

            binary = binaryEntity.getBinary() + binary
        
        return BinaryEntity.createEntity(binary)
            
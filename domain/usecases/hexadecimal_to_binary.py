from abc import ABC, abstractmethod
from unicodedata import decimal
from domain.constants.hexadecimal import HEXADECIMAL
from domain.entities.binary import BinaryEntity
from domain.entities.decimal import DecimalEntity

from domain.entities.hexadecimal import HexadecimalEntity
from domain.errors.hexadecimal_is_not_legit import HexadecimalIsNotLegitError
from domain.errors.something_went_wrong import SomethingWentWrong
from domain.usecases.decimal_to_binary import DecimalToBinaryUsecase


class HexadecimalToBinaryUsecase(ABC):
    @abstractmethod
    def call(self, hexadecimal: str):
        pass


class ImplHexadecimalToBinaryUsecase(HexadecimalToBinaryUsecase):
    def __init__(self, decimalToBinaryUsecase: DecimalToBinaryUsecase):
        self._decimalToBinaryUsecase = decimalToBinaryUsecase

    def call(self, hexadecimal: str):
        try:
            hexadecimalEntityOrError = HexadecimalEntity.createEntity(
                hexadecimal
            )

            if type(hexadecimalEntityOrError) is HexadecimalIsNotLegitError:
                return hexadecimalEntityOrError

            return self._convertingHexadecimalToBinary(hexadecimalEntityOrError)
        except:
            return SomethingWentWrong()

    def _convertingHexadecimalToBinary(self, hexadecimalEntity: HexadecimalEntity):
        hexadecimal = hexadecimalEntity.getHexadecimal()
        hexadecimal_length = hexadecimalEntity.getLength()
        binary = ''

        for i in range(hexadecimal_length, -1, -1):
            decimal = HEXADECIMAL.index(hexadecimal[i])

            binaryEntity = self._decimalToBinaryUsecase.call(decimal, 4)

            binary = binaryEntity.getBinary() + binary

        return BinaryEntity.createEntity(binary)

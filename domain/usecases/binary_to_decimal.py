from abc import ABC, abstractmethod
from domain.entities.binary import BinaryEntity
from domain.entities.decimal import DecimalEntity


class BinaryToDecimalUsecase(ABC):
    @abstractmethod
    def call(self, binaryEntity: BinaryEntity):
        pass


class ImplBinaryToDecimalUsecase(BinaryToDecimalUsecase):
    def call(self, binaryEntity: BinaryEntity):
        binary: str = binaryEntity.getBinary()

        binary_length: int = binary.__len__() - 1

        decimal: int = 0

        for i in range(binary_length, -1, -1):
            if binary[i] == '1':
                decimal += 2**(binary_length - i)

        return DecimalEntity.createEntity(decimal)

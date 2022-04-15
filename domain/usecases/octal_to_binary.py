from abc import abstractmethod
from domain.entities.binary import BinaryEntity
from domain.entities.decimal import DecimalEntity

from domain.entities.octal import OctalEntity
from domain.usecases.decimal_to_binary import DecimalToBinaryUsecase

class OctalToBinaryUsecase:
    @abstractmethod
    def call(octalEntity: OctalEntity):
        pass

class ImplOctalToBinaryUsecase(OctalToBinaryUsecase):
    def __init__(self, decimalToBinaryUsecase: DecimalToBinaryUsecase):
        self._decimalToBinaryUsecase = decimalToBinaryUsecase

    def call(self, octalEntity: OctalEntity):
        octal = octalEntity.getOctal()
        octal_length = octal.__len__() - 1

        binary = ''

        for i in range(octal_length, -1, -1):
            decimalEntity = DecimalEntity.createEntity(int(octal[i]))
            binaryEntity = self._decimalToBinaryUsecase.call(decimalEntity, 3)

            binary = binaryEntity.getBinary() + binary

        return BinaryEntity.createEntity(binary)

from abc import ABC, abstractmethod
from domain.entities.binary import BinaryEntity
from domain.entities.decimal import DecimalEntity

from domain.entities.octal import OctalEntity
from domain.errors.octal_is_not_legit import OctalIsNotLegitError
from domain.errors.something_went_wrong import SomethingWentWrong
from domain.usecases.decimal_to_binary import DecimalToBinaryUsecase

class OctalToBinaryUsecase(ABC):
    @abstractmethod
    def call(octal: str):
        pass

class ImplOctalToBinaryUsecase(OctalToBinaryUsecase):
    def __init__(self, decimalToBinaryUsecase: DecimalToBinaryUsecase):
        self._decimalToBinaryUsecase = decimalToBinaryUsecase

    def call(self, octal: str):
        try:
            octalEntityOrError = OctalEntity.createEntity(octal)

            if type(octalEntityOrError) is OctalIsNotLegitError:
                return octalEntityOrError

            return self._convertingOctalToBinary(octalEntityOrError)      
        except:
            return SomethingWentWrong()
    
    def _convertingOctalToBinary(self, octalEntity: OctalEntity):
        octal = octalEntity.getOctal()
        octal_length = octalEntity.getLength()

        binary = ''

        for i in range(octal_length, -1, -1):
            binaryEntity = self._decimalToBinaryUsecase.call(int(octal[i]), 3)

            binary = binaryEntity.getBinary() + binary

        return BinaryEntity.createEntity(binary)

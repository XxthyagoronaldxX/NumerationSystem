from abc import ABC, abstractmethod
from domain.entities.binary import BinaryEntity
from domain.entities.decimal import DecimalEntity
from domain.errors.binary_is_not_legit import BinaryIsNotLegitError
from domain.errors.something_went_wrong import SomethingWentWrong


class BinaryToDecimalUsecase(ABC):
    @abstractmethod
    def call(self, binary: str):
        pass


class ImplBinaryToDecimalUsecase(BinaryToDecimalUsecase):
    def call(self, binary: str):
        try:
            binaryEntityOrError = BinaryEntity.createEntity(binary)

            if type(binaryEntityOrError) is BinaryIsNotLegitError:
                return binaryEntityOrError

            return self._convertingBinaryToDecimal(binaryEntityOrError)
        except:
            return SomethingWentWrong()
    
    def _convertingBinaryToDecimal(self, binaryEntity: BinaryEntity):
        binary: str = binaryEntity.getBinary()
        binary_length: int = binaryEntity.getLength()
        decimal: int = 0

        for i in range(binary_length, -1, -1):
            bit = binary[i]

            if bit == '1':
                decimal += 2**(binary_length - i)
        
        return DecimalEntity.createEntity(decimal)

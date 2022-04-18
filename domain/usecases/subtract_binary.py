from abc import ABC, abstractmethod
from domain.entities.binary import BinaryEntity
from domain.errors.binary_is_not_legit import BinaryIsNotLegitError
from domain.errors.something_went_wrong import SomethingWentWrong

from domain.usecases.sum_binary import SumBinaryUsecase


class SubtractBinaryUsecase(ABC):
    @abstractmethod
    def call(self, binary01: str, binary02: str):
        pass

class ImplSubtractBinaryUsecase(SubtractBinaryUsecase):
    def __init__(self, sumBinaryUsecase: SumBinaryUsecase):
        self._sumBinaryUsecase = sumBinaryUsecase
    
    def call(self, binary01: str, binary02: str):
        try:
            binaryEntityOrError01 = BinaryEntity.createEntity(binary01)
            binaryEntityOrError02 = BinaryEntity.createEntity(binary02)
            
            if type(binaryEntityOrError01) is BinaryIsNotLegitError or type(binaryEntityOrError02) is BinaryIsNotLegitError:
                return BinaryIsNotLegitError()

            return self._subtractBinary(binaryEntityOrError01, binaryEntityOrError02)
        except:
            return SomethingWentWrong()
        
    def _complementOne(self, binary: str):
        result = ''

        for bit in binary:
            result = result + ('1' if bit == '0' else '0')
        
        return result
        
    def _complementTwo(self, binary: str):
        resultBinaryEntity = self._sumBinaryUsecase.call(binary, '1')

        return resultBinaryEntity.getBinary()
    
    def _complementThree(self, binary: str):
        return binary[1:binary.__len__()]

    def _subtractBinary(self, binaryEntity01: BinaryEntity, binaryEntity02: BinaryEntity):
        binary01 = binaryEntity01.getBinary()
        binary02 = binaryEntity02.getBinary()
        
        #binary02 = (binaryEntity01.getLength() - binaryEntity02.getLength())
        binary02 = self._complementOne(binary02)
        binary02 = self._complementTwo(binary02)

        resultBinaryEntity = self._sumBinaryUsecase.call(binary01, binary02)

        result = self._complementThree(resultBinaryEntity.getBinary())

        return BinaryEntity.createEntity(result)


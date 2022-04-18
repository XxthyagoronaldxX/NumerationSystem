from abc import ABC, abstractmethod
from domain.entities.binary import BinaryEntity
from domain.errors.binary_is_not_legit import BinaryIsNotLegitError
from domain.errors.something_went_wrong import SomethingWentWrong
from domain.usecases.sum_binary import SumBinaryUsecase


class MultiplyBinaryUsecase(ABC):
    @abstractmethod
    def call(self, binary01: str, binary02: str):
        pass


class ImplMultiplyBinaryUsecase(MultiplyBinaryUsecase):
    def __init__(self, sumBinaryUsecase: SumBinaryUsecase):
        self._sumBinaryUsecase = sumBinaryUsecase

    def call(self, binary01: str, binary02: str):
        try:
            binaryEntityOrError01 = BinaryEntity.createEntity(binary01)
            binaryEntityOrError02 = BinaryEntity.createEntity(binary02)

            if type(binaryEntityOrError01) is BinaryIsNotLegitError or type(binaryEntityOrError02) is BinaryIsNotLegitError:
                return BinaryIsNotLegitError()

            return self._multiplyBinary(binaryEntityOrError01, binaryEntityOrError02)
        except:
            return SomethingWentWrong()

    def _multiplyBinary(self, binaryEntity01: BinaryEntity, binaryEntity02: BinaryEntity):
        binary01 = binaryEntity01.getBinary()
        binary02 = binaryEntity02.getBinary()
        binary_result = ''
        binary01_length = binaryEntity01.getLength()
        binary02_length = binaryEntity02.getLength()
        binary_aux = ''

        for i in range(binary01_length, -1, -1): 
            if binary01[i] == '0':
                binary_aux = '0'*binary02_length 
            else:
                binary_aux = binary02

            binary_aux = binary_aux + ((binary01_length - i) * '0')

            if not binary_result:
                binary_result = binary_aux
            else:
                binaryEntity = self._sumBinaryUsecase.call(binary_result, binary_aux)
                binary_result = binaryEntity.getBinary()

        return BinaryEntity.createEntity(binary_result)

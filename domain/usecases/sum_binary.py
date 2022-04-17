from abc import ABC, abstractmethod

from domain.entities.binary import BinaryEntity
from domain.errors.binary_is_not_legit import BinaryIsNotLegitError
from domain.errors.something_went_wrong import SomethingWentWrong


class SumBinaryUsecase(ABC):
    @abstractmethod
    def call(self, binary01: str, binary02: str):
        pass


class ImplSumBinaryUsecase(SumBinaryUsecase):
    def call(self, binary01: str, binary02: str):
        try:
            binaryEntityOrError01 = BinaryEntity.createEntity(binary01)
            binaryEntityOrError02 = BinaryEntity.createEntity(binary02)

            if type(binaryEntityOrError01) is BinaryIsNotLegitError or type(binaryEntityOrError02) is BinaryIsNotLegitError:
                return BinaryIsNotLegitError()

            return self._sumBinary(binaryEntityOrError01, binaryEntityOrError02)
        except:
            return SomethingWentWrong()
    
    def _sumBinary(self, binaryEntity01: BinaryEntity, binaryEntity02: BinaryEntity):
        binary01 = binaryEntity01.getBinary()
        binary02 = binaryEntity02.getBinary()
        go_one = False
        sum_binary = ''

        if binary01.__len__() > binary02.__len__():
            binary02 = '0'*(binary01.__len__()-binary02.__len__()) + binary02
        else:
            binary01 = '0'*(binary02.__len__()-binary01.__len__()) + binary01

        for i in range(binary01.__len__()-1, -1, -1):
            if binary01[i] == binary02[i]:
                if binary01[i] == '0':
                    if go_one:
                        sum_binary = '1' + sum_binary
                        go_one = False
                    else:
                        sum_binary = '0' + sum_binary
                else:
                    sum_binary = ('1' if go_one else '0') + sum_binary
                    go_one = True

            if binary01[i] != binary02[i]:
                if go_one:
                    sum_binary = '0' + sum_binary
                    go_one = True
                else:
                    sum_binary = '1' + sum_binary
        
        if go_one: sum_binary = '1' + sum_binary
        
        return BinaryEntity.createEntity(sum_binary)


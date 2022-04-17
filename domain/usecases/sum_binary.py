from abc import ABC, abstractmethod

from domain.entities.binary import BinaryEntity


class SumBinaryUsecase(ABC):
    @abstractmethod
    def call(self, binaryEntity01: BinaryEntity, binaryEntity02: BinaryEntity):
        pass


class ImplSumBinaryUsecase(SumBinaryUsecase):
    def call(self, binaryEntity01: BinaryEntity, binaryEntity02: BinaryEntity):
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


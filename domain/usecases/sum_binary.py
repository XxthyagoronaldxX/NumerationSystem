from abc import abstractmethod

from domain.entities.binary import BinaryEntity


class SumBinaryUsecase:
    @abstractmethod
    def call(self, binaryEntity01: BinaryEntity, binaryEntity02: BinaryEntity):
        pass


class ImplSumBinaryUsecase(SumBinaryUsecase):
    def call(self, binaryEntity01: BinaryEntity, binaryEntity02: BinaryEntity):
        binary01 = binaryEntity01.getBinary()
        binary02 = binaryEntity02.getBinary()
        binary_length = (binary01.__len__() if binary01.__len__() > binary02.__len__() else binary02.__len__()) - 1
        sum_binary = ''

        for i in range(binary_length, -1, -1):
            if binary01[i] == binary02[i]:
                if binary01[i] == '0':
                    sum_binary = '0' + sum_binary
                else:
                    sum_binary = '10' + sum_binary
            
            if binary01[i] != binary02[i]:
                sum_binary = '1' + sum_binary
        
        return sum_binary


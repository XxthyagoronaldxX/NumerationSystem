from abc import ABC, abstractmethod
from domain.constants.hexadecimal import HEXADECIMAL_FLAG_STOP, HEXADECIMAL
from domain.entities.binary import BinaryEntity
from domain.entities.hexadecimal import HexadecimalEntity


class BinaryToHexadecimalUsecase(ABC):
    @abstractmethod
    def call(self, binaryEntity: BinaryEntity):
        pass


class ImplBinaryToHexadecimalUsecase(BinaryToHexadecimalUsecase):
    def call(self, binaryEntity: BinaryEntity):
        binary = binaryEntity.getBinary()
        binary_length = binary.__len__() - 1

        cont_flag = 0
        hexadecimal = ''
        sum = 0

        for i in range(binary_length, -1, -1):
            if binary[i] == '1':
                sum += 2**cont_flag

            cont_flag += 1

            if cont_flag > HEXADECIMAL_FLAG_STOP:
                hexadecimal = HEXADECIMAL[sum] + hexadecimal

                sum = 0
                cont_flag = 0

        hexadecimal = (str(sum) if sum != 0 else '') + hexadecimal

        return HexadecimalEntity.createEntity(hexadecimal)

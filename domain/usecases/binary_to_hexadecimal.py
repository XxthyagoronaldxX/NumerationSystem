from abc import abstractmethod
from domain.constants.hexadecimal import FLAG_STOP, HEXADECIMAL
from domain.entities.binary import BinaryEntity
from domain.entities.hexadecimal import HexadecimalEntity


class BinaryToHexadecimal:
    @abstractmethod
    def call(self, binaryEntity: BinaryEntity):
        pass


class ImplBinaryToHexadecimal(BinaryToHexadecimal):
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

            if cont_flag > FLAG_STOP:
                hexadecimal += HEXADECIMAL[sum]

                sum = 0
                cont_flag = 0

        return HexadecimalEntity.createEntity(''.join(reversed(hexadecimal)))

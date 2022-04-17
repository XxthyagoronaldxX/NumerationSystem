from abc import ABC, abstractmethod
from domain.constants.hexadecimal import HEXADECIMAL_FLAG_STOP, HEXADECIMAL
from domain.entities.binary import BinaryEntity
from domain.entities.hexadecimal import HexadecimalEntity
from domain.errors.binary_is_not_legit import BinaryIsNotLegitError
from domain.errors.something_went_wrong import SomethingWentWrong


class BinaryToHexadecimalUsecase(ABC):
    @abstractmethod
    def call(self, binary: str):
        pass


class ImplBinaryToHexadecimalUsecase(BinaryToHexadecimalUsecase):
    def call(self, binary: str):
        try:
            binaryEntityOrError = BinaryEntity.createEntity(binary)

            if type(binaryEntityOrError) is BinaryIsNotLegitError:
                return binaryEntityOrError

            return self._convertingBinaryToHexadecimal(binaryEntityOrError)
        except:
            return SomethingWentWrong()
       
    def _convertingBinaryToHexadecimal(self, binaryEntity: BinaryEntity):
        binary = binaryEntity.getBinary()
        binary_length = binaryEntity.getLength()

        cont_flag = 0
        hexadecimal = ''
        sum_each_hexadecimal = 0

        for i in range(binary_length, -1, -1):
            if binary[i] == '1':
                sum_each_hexadecimal += 2**cont_flag

            cont_flag += 1

            if cont_flag > HEXADECIMAL_FLAG_STOP:
                hexadecimal = HEXADECIMAL[sum_each_hexadecimal] + hexadecimal

                sum_each_hexadecimal = 0
                cont_flag = 0

        hexadecimal = (str(sum_each_hexadecimal) if sum_each_hexadecimal != 0 else '') + hexadecimal

        return HexadecimalEntity.createEntity(hexadecimal)

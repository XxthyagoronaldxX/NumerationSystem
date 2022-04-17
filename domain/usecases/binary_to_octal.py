from abc import ABC, abstractmethod
from domain.constants.octal import OCTAL_FLAG_STOP
from domain.entities.binary import BinaryEntity
from domain.entities.octal import OctalEntity
from domain.errors.binary_is_not_legit import BinaryIsNotLegitError
from domain.errors.something_went_wrong import SomethingWentWrong


class BinaryToOctalUsecase(ABC):
    @abstractmethod
    def call(binary: str):
        pass


class ImplBinaryToOctalUsecase(BinaryToOctalUsecase):
    def call(self, binary: str):
        try:
            binaryEntityOrError = BinaryEntity.createEntity(binary)

            if type(binaryEntityOrError) is BinaryIsNotLegitError:
                return binaryEntityOrError

            return self._convertingBinaryToOctal(binaryEntityOrError)
        except:
            return SomethingWentWrong()

    def _convertingBinaryToOctal(self, binaryEntity: BinaryEntity):
        binary = binaryEntity.getBinary()
        binary_length = binaryEntity.getLength()

        octal = ''
        sum_each_octal = 0
        cont_flag = 0

        for i in range(binary_length, -1, -1):
            if binary[i] == '1':
                sum_each_octal += 2**cont_flag

            cont_flag += 1

            if cont_flag > OCTAL_FLAG_STOP:
                cont_flag = 0
                octal = str(sum_each_octal) + octal
                sum_each_octal = 0

        octal = (str(sum_each_octal) if sum_each_octal != 0 else '') + octal

        return OctalEntity.createEntity(octal)

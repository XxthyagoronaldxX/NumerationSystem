from abc import ABC, abstractmethod
from domain.constants.octal import OCTAL_FLAG_STOP
from domain.entities.binary import BinaryEntity
from domain.entities.octal import OctalEntity

class BinaryToOctalUsecase(ABC):
    @abstractmethod
    def call(binaryEntity: BinaryEntity):
        pass

class ImplBinaryToOctalUsecase(BinaryToOctalUsecase):
    def call(self, binaryEntity: BinaryEntity):
        binary = binaryEntity.getBinary()
        binary_length = binary.__len__() - 1

        octal = ''
        sum = 0
        cont_flag = 0

        for i in range(binary_length, -1, -1):
            if binary[i] == '1':
                sum += 2**cont_flag

            cont_flag += 1

            if cont_flag > OCTAL_FLAG_STOP:
                cont_flag = 0
                octal = str(sum) + octal
                sum = 0
        
        octal = (str(sum) if sum != 0 else '') + octal

        return OctalEntity.createEntity(octal)


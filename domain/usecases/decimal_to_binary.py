from abc import abstractmethod
from domain.entities.decimal import DecimalEntity

class DecimalToBinaryUsecase:
  @abstractmethod
  def call(self, decimal):
    pass

class ImplDecimalToBinaryUsecase(DecimalToBinaryUsecase):
  def call(self, decimalEntity: DecimalEntity):
    decimal = decimalEntity.getDecimal()
    binary = ''

    while decimal > 0:
      if decimal % 2 != 0:
        binary += '1'
      else:
        binary += '0'

      decimal = round(decimal/2)

    return ''.join(reversed(binary))
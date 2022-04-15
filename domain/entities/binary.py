from domain.errors.binary_is_not_legit import BinaryIsNotLegitError


class BinaryEntity:
  def __init__(self, binary: str):
    self._binary = binary 

  @staticmethod
  def __binaryIsLegit(binary: str):
    for i in binary:
      if i != '0' and i != '1':
        return False

    return True
  
  @staticmethod
  def createEntity(binary: str):
    if not BinaryEntity.__binaryIsLegit(binary):
      return BinaryIsNotLegitError()

    return BinaryEntity(binary)

  def getBinary(self):
    return self._binary

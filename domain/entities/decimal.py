class DecimalEntity:
  def __init__(self, decimal: int):
    self._decimal = decimal

  @staticmethod
  def createEntity(decimal: int):
    return DecimalEntity(decimal)

  def getDecimal(self):
    return self._decimal

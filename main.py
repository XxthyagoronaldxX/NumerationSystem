from domain.entities.binary import BinaryEntity
from domain.entities.decimal import DecimalEntity
from domain.usecases.binary_to_decimal import ImplBinaryToDecimalUsecase
from domain.usecases.decimal_to_binary import ImplDecimalToBinaryUsecase

binary01 = BinaryEntity.createEntity('10010111')
decimal01 = DecimalEntity.createEntity(10)

decimalToBinaryUsecase = ImplDecimalToBinaryUsecase()

result01 = decimalToBinaryUsecase.call(decimal01)

binaryToDecimalUsecase = ImplBinaryToDecimalUsecase()

result02 = binaryToDecimalUsecase.call(binary01)

print(result01)
print(result02)


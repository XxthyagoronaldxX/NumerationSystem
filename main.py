from domain.entities.binary import BinaryEntity
from domain.entities.decimal import DecimalEntity
from domain.usecases.binary_to_decimal import ImplBinaryToDecimalUsecase
from domain.usecases.binary_to_hexadecimal import ImplBinaryToHexadecimal
from domain.usecases.decimal_to_binary import ImplDecimalToBinaryUsecase
from domain.usecases.hexadecimal_to_binary import ImplHexadecimalToBinary

binary01 = BinaryEntity.createEntity('10010111')
binary02 = BinaryEntity.createEntity('11111011')
decimal01 = DecimalEntity.createEntity(10)

decimalToBinaryUsecase = ImplDecimalToBinaryUsecase()

result01 = decimalToBinaryUsecase.call(decimal01)

binaryToDecimalUsecase = ImplBinaryToDecimalUsecase()

result02 = binaryToDecimalUsecase.call(binary01)

binaryToHexadecimal = ImplBinaryToHexadecimal()

result03 = binaryToHexadecimal.call(binary02)

hexadecimalToBinary = ImplHexadecimalToBinary(decimalToBinaryUsecase)

result04 = hexadecimalToBinary.call(result03)

print(result01.getBinary())
print(result02.getDecimal())
print(result03.getHexadecimal())
print(result04.getBinary())


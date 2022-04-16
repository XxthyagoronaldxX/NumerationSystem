import os
from domain.usecases.sum_binary import ImplSumBinaryUsecase
from domain.entities.decimal import DecimalEntity
from domain.entities.hexadecimal import HexadecimalEntity
from domain.entities.octal import OctalEntity
from domain.errors.binary_is_not_legit import BinaryIsNotLegitError
from domain.errors.hexadecimal_is_not_legit import HexadecimalIsNotLegitError
from domain.errors.octal_is_not_legit import OctalIsNotLegitError
from domain.usecases.binary_to_hexadecimal import ImplBinaryToHexadecimalUsecase
from domain.usecases.binary_to_octal import ImplBinaryToOctalUsecase
from domain.usecases.decimal_to_binary import DecimalToBinaryUsecase, ImplDecimalToBinaryUsecase
from domain.usecases.hexadecimal_to_binary import ImplHexadecimalToBinaryUsecase
from domain.usecases.octal_to_binary import ImplOctalToBinaryUsecase
from presentation.config.option_main import *
from domain.entities.binary import BinaryEntity
from domain.usecases.binary_to_decimal import ImplBinaryToDecimalUsecase

def main():
    decimalToBinaryUsecase: DecimalToBinaryUsecase = ImplDecimalToBinaryUsecase()
    option = DEFAULT_OPTION

    while(option != EXIT):
        os.system('cls') or None
        print('===================================================')
        print('====      By TCKUBIRIM - NumerationSystem      ====')
        print('===================================================')
        print('{} - Binary to decimal.'.format(BINARY_TO_DECIMAL))
        print('{} - Binary to hexadecimal.'.format(BINARY_TO_HEXADECIMAL))
        print('{} - Binary to octal.'.format(BINARY_TO_OCTAL))
        print('{} - Decimal to binary.'.format(DECIMAL_TO_BINARY))
        print('{} - Hexadecimal to binary.'.format(HEXADECIMAL_TO_BINARY))
        print('{} - Octal to binary.'.format(OCTAL_TO_BINARY))
        print('{} - Sair.'.format(EXIT))
        option = input('Escolha uma opção: ')

        os.system('cls') or None
        if option == BINARY_TO_DECIMAL:
            binary = input('Informe o valor em binário para fazer a conversão (Binary to Decimal): ')
            
            binaryEntityOrError = BinaryEntity.createEntity(binary)

            if type(binaryEntityOrError) is BinaryIsNotLegitError:
                print('Você deve inserir um valor em binário válido!')
            elif type(binaryEntityOrError) is BinaryEntity:
                decimalEntity = ImplBinaryToDecimalUsecase().call(binaryEntityOrError)

                print('O valor convertido [{}] em decimal é: {}'.format(binary, decimalEntity.getDecimal()))
        elif option == BINARY_TO_HEXADECIMAL:
            binary = input('Informe o valor em binário para fazer a conversão (Binary to Hexadecimal): ')
            
            binaryEntityOrError = BinaryEntity.createEntity(binary)

            if type(binaryEntityOrError) is BinaryIsNotLegitError:
                print('Você deve inserir um valor em binário válido!')
            elif type(binaryEntityOrError) is BinaryEntity:
                hexadecimalEntity = ImplBinaryToHexadecimalUsecase().call(binaryEntityOrError)

                print('O valor convertido [{}] em Hexadecimal é: {}'.format(binary, hexadecimalEntity.getHexadecimal()))
        elif option == BINARY_TO_OCTAL:
            binary = input('Informe o valor em binário para fazer a conversão (Binary to Octal): ')
            
            binaryEntityOrError = BinaryEntity.createEntity(binary)

            if type(binaryEntityOrError) is BinaryIsNotLegitError:
                print('Você deve inserir um valor em binário válido!')
            elif type(binaryEntityOrError) is BinaryEntity:
                hexadecimalEntity = ImplBinaryToOctalUsecase().call(binaryEntityOrError)

                print('O valor convertido [{}] em Octal é: {}'.format(binary, hexadecimalEntity.getOctal()))
        elif option == DECIMAL_TO_BINARY:
            decimal = int(input('Informe o valor em Decimal para fazer a conversão (Decimal to binary): '))

            decimalEntity = DecimalEntity.createEntity(decimal)

            binaryEntity = ImplDecimalToBinaryUsecase().call(decimalEntity)

            print('O valor convertido [{}] em Binario é: {}'.format(decimal, binaryEntity.getBinary()))
        elif option == HEXADECIMAL_TO_BINARY:
            hexadecimal = input('Informe o valor em Hexadecimal para fazer a conversão (Hexadecimal to binary): ')

            hexadecimalEntityOrError = HexadecimalEntity.createEntity(hexadecimal)

            if type(hexadecimalEntityOrError) is HexadecimalIsNotLegitError:
                print('Você deve inserir um valor em Hexadecimal válido!')
            elif type(hexadecimalEntityOrError) is HexadecimalEntity:
                binaryEntity = ImplHexadecimalToBinaryUsecase(decimalToBinaryUsecase).call(hexadecimalEntityOrError)

                print('O valor convertido [{}] em Binario é: {}'.format(hexadecimal, binaryEntity.getBinary()))
        elif option == OCTAL_TO_BINARY:
            octal = input('Informe o valor em Octal para fazer a conversão (Octal to binary): ')

            octalEntityOrError = OctalEntity.createEntity(octal)

            if type(octalEntityOrError) is OctalIsNotLegitError:
                print('Você deve inserir um valor em Octal válido!')
            elif type(octalEntityOrError) is OctalEntity:
                binaryEntity = ImplOctalToBinaryUsecase(decimalToBinaryUsecase).call(octalEntityOrError)

                print('O valor convertido [{}] em Binario é: {}'.format(octal, binaryEntity.getBinary()))

        os.system('pause')


binary01 = BinaryEntity.createEntity('1011')
binary02 = BinaryEntity.createEntity('1001')
usecase = ImplSumBinaryUsecase()
result = usecase.call(binary01, binary02)
print(result)
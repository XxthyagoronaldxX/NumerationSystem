from decimal import Decimal
import os
from domain.usecases.multiply_binary import ImplMultiplyBinaryUsecase
from domain.usecases.sum_binary import ImplSumBinaryUsecase, SumBinaryUsecase
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

decimalToBinaryUsecase: DecimalToBinaryUsecase = ImplDecimalToBinaryUsecase()
sumBinaryUsecase: SumBinaryUsecase = ImplSumBinaryUsecase()

def screenTitle():
    print('===================================================')
    print('====      By TCKUBIRIM - NumerationSystem      ====')
    print('===================================================')


def screenOptions():
    print('{} - Binary to decimal.'.format(BINARY_TO_DECIMAL))
    print('{} - Binary to hexadecimal.'.format(BINARY_TO_HEXADECIMAL))
    print('{} - Binary to octal.'.format(BINARY_TO_OCTAL))
    print('{} - Decimal to binary.'.format(DECIMAL_TO_BINARY))
    print('{} - Hexadecimal to binary.'.format(HEXADECIMAL_TO_BINARY))
    print('{} - Octal to binary.'.format(OCTAL_TO_BINARY))
    print('{} - Sum binary.'.format(SUM_BINARY))
    print('{} - Multiply binary.'.format(MULTIPLY_BINARY))
    print('{} - Sair.'.format(EXIT))


def binaryToDecimal():
    binary = input(
        'Informe o valor em binário para fazer a conversão (Binary to Decimal): ')

    decimalEntityOrError = ImplBinaryToDecimalUsecase().call(binary)

    if type(decimalEntityOrError) is DecimalEntity:
        print('O valor convertido [{}] em decimal é: {}'.format(
            binary, decimalEntityOrError.getDecimal()
        ))
    else:
        print(decimalEntityOrError)


def binaryToHexadecimal():
    binary = input(
        'Informe o valor em binário para fazer a conversão (Binary to Hexadecimal): ')

    hexadecimalEntityOrError = ImplBinaryToHexadecimalUsecase().call(binary)

    if type(hexadecimalEntityOrError) is HexadecimalEntity:
        print('O valor convertido [{}] em Hexadecimal é: {}'.format(
            binary, hexadecimalEntityOrError.getHexadecimal()))
    else:
        print(hexadecimalEntityOrError)


def binaryToOctal():
    binary = input(
        'Informe o valor em binário para fazer a conversão (Binary to Octal): ')

    octalEntityOrError = ImplBinaryToOctalUsecase().call(binary)

    if type(octalEntityOrError) is OctalEntity:
        print('O valor convertido [{}] em Octal é: {}'.format(
            binary, octalEntityOrError.getOctal()))
    else:
        print(octalEntityOrError)


def decimalToBinary():
    decimal = int(
        input('Informe o valor em Decimal para fazer a conversão (Decimal to binary): '))

    binaryEntityOrError = ImplDecimalToBinaryUsecase().call(decimal)

    if type(binaryEntityOrError) is BinaryEntity:
        print('O valor convertido [{}] em Binario é: {}'.format(
            decimal, binaryEntityOrError.getBinary()))
    else:
        print(binaryEntityOrError)


def hexadecimalToBinary():
    hexadecimal = input(
        'Informe o valor em Hexadecimal para fazer a conversão (Hexadecimal to binary): '
    )

    binaryEntityOrError = ImplHexadecimalToBinaryUsecase(decimalToBinaryUsecase).call(hexadecimal)

    if type(binaryEntityOrError) is BinaryEntity:
        print('O valor convertido [{}] em Binario é: {}'.format(
            hexadecimal, binaryEntityOrError.getBinary()))
    else:
        print(binaryEntityOrError)


def octalToBinary():
    octal = input(
        'Informe o valor em Octal para fazer a conversão (Octal to binary): ')

    binaryEntityOrError = ImplOctalToBinaryUsecase(
        decimalToBinaryUsecase).call(octal)

    if type(binaryEntityOrError) is BinaryEntity:
        print('O valor convertido [{}] em Binario é: {}'.format(
            octal, binaryEntityOrError.getBinary()))
    else:
        print(binaryEntityOrError)


def sumBinary():
    binary01 = input(
        'Informe o primeiro Binário para ser realizado a soma: ')
    binary02 = input(
        'Informe o segundo Binário para ser realizado a soma: ')

    binaryEntityOrError = ImplSumBinaryUsecase().call(binary01, binary02)

    if type(binaryEntityOrError) is BinaryEntity:
        print('O valor resultante da soma entre [ {} + {} ] é igual a: {}'.format(
            binary01, binary02, binaryEntityOrError.getBinary()))
    else:
        print(binaryEntityOrError)


def multiplyBinary():
    binary01 = input(
        'Informe o primeiro Binário para ser realizado a multiplicação: ')
    binary02 = input(
        'Informe o segundo Binário para ser realizado a multiplicação: ')

    binaryEntityOrError = ImplMultiplyBinaryUsecase(sumBinaryUsecase).call(binary01, binary02)

    if type(binaryEntityOrError) is BinaryEntity:
        print('O valor resultante da multiplicação entre [ {} + {} ] é igual a: {}'.format(
            binary01, binary02, binaryEntityOrError.getBinary()))
    else:
        print(binaryEntityOrError)

def main():
    option = DEFAULT_OPTION

    while(option != EXIT):
        os.system('cls') or None
        screenTitle()
        screenOptions()
        option = input('Escolha uma opção: ')

        os.system('cls') or None
        if option == BINARY_TO_DECIMAL:
            binaryToDecimal()
        elif option == BINARY_TO_HEXADECIMAL:
            binaryToHexadecimal()
        elif option == BINARY_TO_OCTAL:
            binaryToOctal()
        elif option == DECIMAL_TO_BINARY:
            decimalToBinary()
        elif option == HEXADECIMAL_TO_BINARY:
            hexadecimalToBinary()
        elif option == OCTAL_TO_BINARY:
            octalToBinary()
        elif option == SUM_BINARY:
            sumBinary()
        elif option == MULTIPLY_BINARY:
            multiplyBinary()
        os.system('pause')


main()

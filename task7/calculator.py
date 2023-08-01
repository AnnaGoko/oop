from abc import ABC, abstractmethod
import logging

logging.basicConfig(filename='calculator.log', level=logging.DEBUG)

class ComplexNumber(ABC):
    @abstractmethod
    def add(self, other):
        pass
    
    @abstractmethod
    def multiply(self, other):
        pass
    
    @abstractmethod
    def divide(self, other):
        pass

class RealNumber(ComplexNumber):
    def __init__(self, real):
        self.real = real
    
    def add(self, other):
        if isinstance(other, RealNumber):
            return RealNumber(self.real + other.real)
        elif isinstance(other, ImaginaryNumber):
            return ComplexNumberFactory.create_complex_number(self.real + other.imaginary, other.imaginary)
    
    def multiply(self, other):
        if isinstance(other, RealNumber):
            return RealNumber(self.real * other.real)
        elif isinstance(other, ImaginaryNumber):
            return ImaginaryNumber(self.real * other.imaginary)
    
    def divide(self, other):
        if isinstance(other, RealNumber):
            return RealNumber(self.real / other.real)
        elif isinstance(other, ImaginaryNumber):
            return ImaginaryNumber(self.real / other.imaginary)
            
class ImaginaryNumber(ComplexNumber):
    def __init__(self, imaginary):
        self.imaginary = imaginary
    
    def add(self, other):
        if isinstance(other, RealNumber):
            return ComplexNumberFactory.create_complex_number(self.imaginary + other.real, self.imaginary)
        elif isinstance(other, ImaginaryNumber):
            return ImaginaryNumber(self.imaginary + other.imaginary)
    
    def multiply(self, other):
        if isinstance(other, RealNumber):
            return ImaginaryNumber(self.imaginary * other.real)
        elif isinstance(other, ImaginaryNumber):
            return RealNumber(-1 * self.imaginary * other.imaginary)
    
    def divide(self, other):
        if isinstance(other, RealNumber):
            return ImaginaryNumber(self.imaginary / other.real)
        elif isinstance(other, ImaginaryNumber):
            return RealNumber(self.imaginary / other.imaginary)

class ComplexNumberFactory:
    @staticmethod
    def create_complex_number(real, imaginary):
        if real == 0:
            return ImaginaryNumber(imaginary)
        elif imaginary == 0:
            return RealNumber(real)
        else:
            return ComplexNumberFactory.create_complex_number(RealNumber(real), ImaginaryNumber(imaginary))

class ComplexCalculator:
    def add(self, num1, num2):
        result = num1.add(num2)
        logging.info(f'{num1} + {num2} = {result}')
        return result
    
    def multiply(self, num1, num2):
        result = num1.multiply(num2)
        logging.info(f'{num1} * {num2} = {result}')
        return result
    
    def divide(self, num1, num2):
        result = num1.divide(num2)
        logging.info(f'{num1} / {num2} = {result}')
        return result
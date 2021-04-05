class ComplexNumber:
    def __init__(self, real_number=0, imaginary_number=0):
        """
        Комплексное число
        """
        self.complex_number = complex(real_number, imaginary_number)

    def __add__(self, other):
        """Сложение комплексных чисел"""
        result = self.complex_number + other.complex_number
        return ComplexNumber(result)

    def __mul__(self, other):
        """Умножение комплексных чисел"""
        result = self.complex_number * other.complex_number
        return ComplexNumber(result)

    def __str__(self):
        return f'{self.complex_number}'


# Проверки
cn_1 = ComplexNumber(10, 5)
cn_2 = ComplexNumber(3, -3)
cn_3 = ComplexNumber(10)

print(cn_1 + cn_2)
print(type(cn_1 + cn_2))

print(cn_1 * cn_2)
print(type(cn_1 * cn_2))

print(cn_1 + cn_3)

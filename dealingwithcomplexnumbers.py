import math


class Complex(object):
    def __init__(self, real, imaginary):
        self.imaginary = imaginary
        self.real = real

    def __add__(self, no):
        add_real = self.real + no.real
        add_imag = self.imaginary + no.imaginary
        return Complex(real = add_real, imaginary = add_imag)

    def __sub__(self, no):
        sub_real = self.real - no.real
        sub_imag = self.imaginary - no.imaginary
        return Complex(real = sub_real, imaginary = sub_imag)

    def __mul__(self, no):
        mul_real = self.real * no.real - self.imaginary * no.imaginary
        mul_imag = self.real * no.imaginary + self.imaginary * no.real
        return Complex(real = mul_real, imaginary = mul_imag)

    def __truediv__(self, no):
        div_real = (self.real*no.real+self.imaginary*no.imaginary) / (no.real**2 + no.imaginary**2)
        div_imag = (self.imaginary*no.real - self.real*no.imaginary) / (no.real**2 + no.imaginary**2)
        return Complex(real = div_real, imaginary = div_imag)

    def mod(self):
        mod = (self.real**2 + self.imaginary**2)**(1/2)
        return Complex(real = mod, imaginary = 0.00)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result


if __name__ == '__main__':
    input_1 = "2 1"
    input_2 = "5 6"
    c = list(map(float, input_1.split()))
    d = list(map(float, input_2.split()))
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x + y, x - y, x * y, x / y, x.mod(), y.mod()]), sep='\n')
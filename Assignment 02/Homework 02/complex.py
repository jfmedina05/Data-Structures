class Complex(object):

    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return Complex(
            self.real + other.real,
            self.imaginary + other.imaginary
        )

    def __mul__(self, other):
        return Complex(
            self.real * other.real - self.imaginary * other.imaginary,
            self.real * other.imaginary + self.imaginary * other.real
        )

    def __str__(self):
        return str(self.real) + " + " + str(self.imaginary) + "i"


a = Complex(2, 3)
b = Complex(4, 5)

print("a =", a)
print("b =", b)
print("a + b =", a + b)
print("a * b =", a * b)

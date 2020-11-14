# Isabella Gomez A15305555
# ECE143 HW7

from fractions import Fraction

class Rational:

    def __init__(self,x,y):
        self.x = x
        self.y = y

        # check that x and y are ints
        assert type(x) == int and type(y) == int

    def __repr__(self):
        divided = Fraction(self.x, self.y)
        if divided._denominator == 1:
            return '%d'%divided._numerator
        return '%d/%d'%(divided._numerator, divided._denominator)

    def __float__(self):
        return float(self.x/self.y)

    def __int__(self):
        return int(self.x/self.y)

    def __mul__(self, other):
        if not isinstance(other, (int, float)):
            simplified = Fraction(self.x * other.x, self.y * other.y)
            return Rational(simplified._numerator, simplified._denominator)
        multiplied = Fraction(self.x,self.y) * Fraction(other)
        return Rational(Fraction(multiplied)._numerator, Fraction(multiplied)._denominator)

    def __add__(self, other):
        added = Fraction(self.x,self.y) + Fraction(other.x, other.y)
        return Rational(Fraction(added)._numerator, Fraction(added)._denominator)

    def __sub__(self, other):
        subbed = Fraction(self.x,self.y) - Fraction(other.x, other.y)
        return Rational(Fraction(subbed)._numerator, Fraction(subbed)._denominator)

    def __truediv__(self, other):
        if not isinstance(other, (int, float)):
            divided = Fraction(other.x,other.y)/Fraction(self.x,self.y)
            return Rational(Fraction(divided)._numerator, Fraction(divided)._denominator)
        divided = Fraction(self.x,self.y) / Fraction(other)
        return Rational(Fraction(divided)._numerator, Fraction(divided)._denominator)

    def __rtruediv__(self, other):
        if not isinstance(other, (int, float)):
            divided = Fraction(other.x, other.y) / Fraction(self.x, self.y)
            return Rational(Fraction(divided)._numerator, Fraction(divided)._denominator)
        fraction1 = Fraction(self.x, self.y)
        faction2 = Fraction(other)
        divided = faction2 / fraction1
        return Rational(Fraction(divided)._numerator, Fraction(divided)._denominator)

    def __neg__(self):
        return Rational(-self.x,self.y)

    def __lt__(self, other):
        fraction2 = Fraction(other.x, other.y)
        fraction1 = Fraction(self.x,self.y)

        if fraction2 < fraction1:
            return False
        elif fraction1 < fraction2:
            return True
        else: # if they are equal do not return anything
            return NotImplemented

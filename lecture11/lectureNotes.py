from math import gcd

class Rational:
    def __init__(self, numerator, denominator):
        g = gcd(numerator, denominator)
        self.numer = numerator // g
        self.denom = denominator // g

    def __str__(self):
        return f"{self.numer}/{self.denom}"

    def __repr__(self):
        return f"Rational({self.numer}, {self.denom})"

    def __add__(self, other):
        new_numer = self.numer * other.denom + other.numer * self.denom
        new_denom = self.denom * other.denom
        return Rational(new_numer, new_denom)


print(Rational(1, 2) + Rational(3, 4))

print(str(Rational(3,4)))
print(str(1))

bool(dumbo)
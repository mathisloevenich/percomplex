import math


class PerComplex:
    """
    Class of percomplex numbers where

    real = real number,
    imag = i, with i^2 = -1
    perplex = p, with p^2 = -1

    and i * p = - p * i,

    which means that the commutative law is not applicative here.

    """

    def __init__(self, real: float, imag: float = 0, perplex: float = 0):
        self.real: float = real
        self.imag: float = imag
        self.perplex: float = perplex

    def __add__(self, other):
        return PerComplex(
            self.real + other.real,
            self.imag + other.imag,
            self.perplex + other.perplex
        )

    def __abs__(self):
        return math.sqrt(
            self.real ** 2 +
            self.imag ** 2 +
            self.perplex ** 2
        )

    @property
    def coordinates(self):
        return self.real, self.imag, self.perplex

    def __repr__(self):
        return (
            f"Real: {self.real}, "
            f"Imag: {self.imag}, "
            f"Perplex: {self.perplex}"
        )

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return PerComplex(
                self.real * other,
                self.imag * other,
                self.perplex * other
            )
        # new perplex number must be within the group
        assert self.imag * other.perplex == self.perplex * other.imag
        new_real = (
                self.real * other.real -
                self.imag * other.imag -
                self.perplex * other.perplex
        )
        new_imag = self.real * other.imag + self.imag * other.real
        new_perplex = self.real * other.perplex + self.perplex * other.real
        return PerComplex(
            new_real,
            new_imag,
            new_perplex
        )

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return PerComplex(
                self.real / other,
                self.imag / other,
                self.perplex / other
            )
        return self * PerComplex(
            other.real,
            - other.imag,
            - other.perplex
        ) / (other.real ** 2 + other.imag ** 2 + other.perplex ** 2)

    def __pow__(self, power):
        new_percomplex = self
        for i in range(1, power):
            new_percomplex *= self
        return new_percomplex

    def get_next_members(self, num):
        """
        Starting with a PerComplex number get the next one in the group
        :return:
        """
        index = 1
        while index < num + 1:
            get_new_perplex = index * self.perplex / self.imag
            yield PerComplex(
                self.real,
                index,
                get_new_perplex
            )
            index += 1



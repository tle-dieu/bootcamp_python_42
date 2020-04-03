from numbers import Number
import numpy as np


class Vector:
    """A class representing a vector

    Attributes:
        values (list): List of values (vector)
        size (int): Size of values

    See help(Vector.__init__) for how to initialize a vector
    """

    def __init__(self, v):
        """Init function of Vector

        Args:
            v (int or tuple or list): Can be size of a Vector,
                a list representing a vector,
                or a tuple representing a range

        Raises:
            ValueError: If v is a int < 0
            TypeError: If v is a list and doesn't contain floats
            ValueError: If v is a tuple and its size != 2
            TypeError: If v is a tuple and doesn't contain ints
            TypeError: If v is neither a tuple nor a list
                       nor an int nor a Vector

        See help(Vector) for more info about Vector
        """
        if isinstance(v, int):
            if v < 0:
                raise ValueError("size is less than zero")
            v = np.arange(0, v, 1.0).tolist()
        elif isinstance(v, list):
            if any(not isinstance(i, float) for i in v):
                raise TypeError("vector elements aren't floats")
        elif isinstance(v, tuple):
            if len(v) != 2:
                raise ValueError("tuple doesn't have a size of two")
            if any(not isinstance(i, int) for i in v):
                raise TypeError("tuple elements aren't ints")
            v = np.arange(*v, 1.0 if v[0] < v[1] else -1.0).tolist()
        else:
            raise TypeError("cannot create a vector with argument of type"
                            f" {type(v)}")
        self.values = v
        self.size = len(self.values)

    def __add__(self, other):
        if isinstance(other, Number):
            return Vector([i + other for i in self.values])
        if not isinstance(other, Vector):
            return NotImplemented
        if other.size != self.size:
            raise ValueError(f"operands could not be broadcast together with "
                             f"size {self.size} and {other.size}")
        return Vector([x + y for x, y in zip(self.values, other.values)])

    def __radd__(self, other):
        if isinstance(other, Number):
            return Vector([other + i for i in self.values])
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Number):
            return Vector([i - other for i in self.values])
        if not isinstance(other, Vector):
            return NotImplemented
        if other.size != self.size:
            raise ValueError(f"operands could not be broadcast together with "
                             f"size {self.size} and {other.size}")
        return Vector([x - y for x, y in zip(self.values, other.values)])

    def __rsub__(self, other):
        if isinstance(other, Number):
            return Vector([other - i for i in self.values])
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, Number):
            return Vector([i / other for i in self.values])
        return NotImplemented

    def __rtruediv__(self, other):
        if isinstance(other, Number):
            return Vector([other / i for i in self.values])
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Number):
            return Vector([i * other for i in self.values])
        if not isinstance(other, Vector):
            return NotImplemented
        if other.size != self.size:
            raise ValueError(f"operands could not be broadcast together with "
                             f"size {self.size} and {other.size}")
        return sum([x * y for x, y in zip(self.values, other.values)])

    def __rmul__(self, other):
        if isinstance(other, Number):
            return Vector([other * i for i in self.values])
        return NotImplemented

    def __str__(self):
        return f'(Vector {self.values})'

    def __repr__(self):
        return f"{self.__class__} ({self.__dict__})"

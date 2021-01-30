from typing import Any
from math import hypot


class Point:
    def __init__(self, x: float = 0.0, y: float = 0.0) -> None:
        self._x = float(x)
        self._y = float(y)

    @property
    def x(self) -> float:
        return self._x

    @property
    def y(self) -> float:
        return self._y

    @x.setter
    def x(self, value: float) -> None:
        self._x = float(value)

    @y.setter
    def y(self, value: float) -> None:
        self._y = float(value)

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'

    def __eq__(self, other: Any) -> bool:
        self.__check_type(other)
        return self.x == other.x and self.y == other.y

    def __ne__(self, other: Any) -> bool:
        return not self == other

    def __check_type(self, other: Any) -> None:
        if not isinstance(other, self.__class__):
            raise TypeError(f'other param should be of type {self.__class__.__name__}')

    def distance(self, other: Any) -> float:
        self.__check_type(other)
        return hypot(self.x - other.x, self.y - other.y)


if __name__ == '__main__':  # pragma: no cover
    point = Point()
    print(point)

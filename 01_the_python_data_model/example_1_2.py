import math


class Vector:
    def __init__(self, x: float = 0, y: float = 0) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Vector({repr(self.x)}, {repr(self.y)})"

    def __abs__(self) -> float:
        return math.hypot(self.x, self.y)

    def __bool__(self) -> bool:
        return bool(abs(self))

    def __add__(self, other: "Vector") -> "Vector":
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)

    def __mul__(self, scalar: float) -> "Vector":
        new_x = self.x * scalar
        new_y = self.y * scalar
        return Vector(new_x, new_y)

    def __eq__(self, other: "Vector") -> bool:
        if isinstance(other, Vector):
            same_x = self.x == other.x
            same_y = self.y == other.y
            return same_x and same_y
        else:
            return False

from example_1_2 import Vector


def test_vector_equality():
    vector_1 = Vector(1, 2)
    vector_2 = Vector(2, 3)
    vector_3 = Vector(2, 3)
    other = "other"

    assert vector_1 != other
    assert vector_1 != vector_2
    assert vector_2 == vector_3


def test_vector_addition():
    vector_1 = Vector(2, 4)
    vector_2 = Vector(2, 1)

    assert vector_1 + vector_2 == Vector(4, 5)


def test_vector_absolute_value():
    vector = Vector(3, 4)
    assert abs(vector) == 5


def test_vector_scalar_multiplication():
    vector = Vector(3, 4)
    assert vector * 3 == Vector(9, 12)
    assert abs(vector * 3) == 15


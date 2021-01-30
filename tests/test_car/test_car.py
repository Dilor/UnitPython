import pytest

from car.car import Car, prettify_string, check_numbers, ToMuchFuel, OutOfFuel
from point.point import Point


@pytest.mark.parametrize('actual, expected', [
    ('MAZDA', 'Mazda'),
    ('MaZDA\n', 'Mazda'),
    ('mazda\t', 'Mazda'),
    ('MAZDA', 'Mazda')
])
def test_prettify_string(actual, expected):
    assert prettify_string(actual) == expected

# def test_prettify_string():
#     assert prettify_string('MAZDA') == 'Mazda'
#     assert prettify_string('MaZDA') == 'Mazda'
#     assert prettify_string('mazda') == 'Mazda'
#     assert prettify_string('Mazda') == 'Mazda'

def test_prettify_string_exception():
    with pytest.raises(TypeError):
        prettify_string(3)


@pytest.mark.parametrize('value, exception_type', [
    (-100, ValueError),
    ('text', ValueError),
    (dir, TypeError)
])
def test_prettify_string(value, exception_type):
    with pytest.raises(exception_type):
        check_numbers(value)


@pytest.mark.parametrize('actual, expected', [
    (100, 100),
    (100.0, 100),
    ('100', 100)
])
def test_check_numbers(actual, expected):
    assert check_numbers(actual) == expected


@pytest.mark.parametrize('value, exception_type', [
    (-100, ValueError),
    ('text', ValueError),
    (dir, TypeError)
])
def test_check_numbers_exception(value, exception_type):
    with pytest.raises(exception_type):
        check_numbers(value)


# def test_check_numbers():
#     assert check_numbers(100) == 100
#     assert check_numbers(100.0) == 100
#     assert check_numbers('100') == 100

def test_check_refill_exception():
    point = Point(4, 4)
    car = Car(30, 90, 10, point, "MAzda")
    with pytest.raises(ToMuchFuel):
        car.refill(100)


def test_fill():
    point1 = Point(4, 4)
    car1 = Car(30, 90, 10, point1, "MAzda")
    car1.refill(10)
    assert car1.fuel_amount == 40


def test_car_to_string():
    point1 = Point(4, 4)
    car1 = Car(30, 90, 10, point1, "MAzda")
    assert str(car1) == 'Mazda: fuel - 30/90, consumption - 10, location - (4.0, 4.0)'


def test_drive():
    point1 = Point(4, 4)
    point2 = Point(5, 5)
    car1 = Car(30, 90, 10, point1, "MAzda")
    car1.drive(point2)
    assert car1.location == point2


def test_check_drive_exception():
    point1 = Point(4, 4)
    point2 = Point(555, 555)
    car1 = Car(30, 90, 10, point1, "MAzda")
    with pytest.raises(OutOfFuel):
        car1.drive(point2)


def test_car_setters():
    point1 = Point(4, 4)
    car1 = Car(30, 90, 10, point1, "MAzda")

    assert car1.fuel_amount == 30
    car1.fuel_amount = 10
    assert car1.fuel_amount == 10

    assert car1.fuel_capacity == 90
    car1.fuel_capacity = 10
    assert car1.fuel_capacity == 10

    assert car1.fuel_consumption == 10
    car1.fuel_consumption = 5
    assert car1.fuel_consumption == 5

    assert car1.model == 'Mazda'
    car1.model = 'Tesla'
    assert car1.model == 'Tesla'


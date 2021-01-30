import pytest

from point.point import Point


@pytest.mark.parametrize('x, y', [
    (0.0, 0.0),
    (1.0, 3.0)
])
def test_point_constructor(x, y):
    point = Point(x, y)
    assert point.x == x
    assert point.y == y


def test_point_setters():
    point = Point()

    point.x = 42
    point.y = 42

    assert point.x == 42.0
    assert point.y == 42.0


@pytest.mark.parametrize('value, exception_type', [
    ('error', ValueError),
    (dir, TypeError)
])
def test_point_setters_exception(value, exception_type):
    point = Point()

    with pytest.raises(exception_type):
        point.x = value

    with pytest.raises(exception_type):
        point.y = value


def test_point_distance():
    p1 = Point()
    p2 = Point(2, 4)

    assert p1.distance(p2) == 4.47213595499958


def test_point_distance_exception():
    with pytest.raises(TypeError):
        p1 = Point()
        p1.distance(dir)


def test_point_to_string():
    point = Point()

    assert str(point) == '(0.0, 0.0)'


def test_point_operators():
    p1 = Point()
    p2 = Point()
    p3 = Point(1, 10)

    assert p1 == p2
    assert not p1 == p3
    assert not p1 != p2
    assert p1 != p3

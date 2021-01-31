import pytest

from pen.pen import Pen, check_numeric, OutOfInk
from paper.paper import Paper


@pytest.mark.parametrize('actual, expected', [
    (100, 100),
    (100.0, 100),
    ('100', 100)
])
def test_check_numeric(actual, expected):
    assert check_numeric(actual) == expected


@pytest.mark.parametrize('value, exception_type', [
    (-100, ValueError),
    ('error', ValueError),
    (dir, TypeError)
])
def test_check_numeric_exception(value, exception_type):
    with pytest.raises(exception_type):
        check_numeric(value)


def pen_constructor():
    a5 = Pen(100)
    assert a5.ink_capacity == 100
    assert a5.ink_amount == 0


def test_pen_setters():
    parker = Pen(10)
    parker.ink_amount = 10
    assert parker.ink_amount == 10

    parker.ink_capacity = 20
    assert parker.ink_capacity == 20


def test_write():
    parker = Pen(4)
    a4 = Paper(100)
    parker.write(a4, 'some long text')
    assert a4.show() == print('some')

    parker.refill()
    parker.write(a4, 't')
    assert parker.ink_amount == 3

    parker1 = Pen(0)
    with pytest.raises(OutOfInk):
        parker1.write(a4, 'text')


def test_pen_to_string():
    parker = Pen(1000)
    assert str(parker) == 'Pen: ink amount - 1000, ink capacity - 1000'

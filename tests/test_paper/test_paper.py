import pytest

from paper.paper import check_numeric, Paper, OutOfSpace


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


def test_paper_constructor():
    a5 = Paper(1000)

    assert a5.symbols == 0
    assert a5.content == ''
    assert a5.max_symbols == 1000


def test_paper_setter():
    a5 = Paper(1000)
    a5.symbols = 300
    assert a5.symbols == 300

    a5.content = 'text'
    assert a5.content == 'text'

    a5.max_symbols = 500
    assert a5.max_symbols == 500


def test_unit_to_string():
    a5 = Paper(2000)

    assert str(a5) == 'Paper: max symbols - 2000, symbols - 0'


def test_add_content():
    a4 = Paper(100)
    a5 = Paper(5)

    a4.add_content('text')
    assert a4.show() == print('text')

    with pytest.raises(OutOfSpace):
        a5.add_content('oh no! this text is so big')
    assert a5.show() == print('it is')


def test_add_content_exception():
    a6 = Paper(3)
    with pytest.raises(OutOfSpace):
        a6.add_content('text')

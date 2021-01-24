import pytest

from unit.unit import Unit, prettify_string, check_numeric, UnitIsDeadException


def test_takeDamage():
    unit1 = Unit('SoLdIeR', 100, 100, 10)
    unit1.takeDamage(40)
    assert unit1.hp == 60

def test_attack():
    unit1 = Unit('SoLdIeR', 100, 100, 10)
    unit2 = Unit('SoLdIeR', 100, 100, 10)
    unit1.attack(unit2)
    assert unit1.hp == 95
    assert unit2.hp == 90


def test_counter_attack_exception():
    with pytest.raises(UnitIsDeadException):
        unit1 = Unit('SoLdIeR', 100, 100, 50)
        unit2 = Unit('SoLdIeR', 100, 100, 210)
        unit1.attack(unit2)

def test_unit_setters():
    unit1 = Unit('SoLdIeR', 100, 100, 10)
    unit1.name = 'Superwarrior'
    unit1.hp = 50
    unit1.maxHP = 60
    unit1.dmg = 14

    assert unit1.name == 'Superwarrior'
    assert unit1.hp == 50
    assert unit1.maxHP == 60
    assert unit1.dmg == 14

@pytest.mark.parametrize('actual, expected', [
    ('SOLDIER', 'Soldier'),
    ('soldier\n', 'Soldier'),
    ('\tSoLdIeR', 'Soldier'),
    (' SoLdIeR ', 'Soldier'),
    ('Soldier', 'Soldier')
])

def test_prettify_string(actual, expected):
    assert prettify_string(actual) == expected


def test_prettify_string_exception():
    with pytest.raises(TypeError):
        prettify_string(10000)

@pytest.mark.parametrize('actual, expected', [
    (100, 100),
    (100.0, 100),
    ('100', 100)
])
def test_check_numeric(actual, expected):
    assert check_numeric(actual) == expected


@pytest.mark.parametrize('value, exception_type', [
    (-100, ValueError),
    (0, ValueError),
    ('error', ValueError),
    (dir, TypeError)
])
def test_check_numeric_exception(value, exception_type):
    with pytest.raises(exception_type):
        check_numeric(value)

import pytest

from unit.unit import prettify_string, check_numeric, UnitIsDeadException, Unit


def test_takeDamage():
    unit1 = Unit('SoLdIeR', 100, 100, 10)
    unit1.takeDamage(40)
    assert unit1.hp == 60


def test_addHitPoints():
    unit1 = Unit('SoLdIeR', 50, 100, 10)
    unit1.addHitPoints(40)
    assert unit1.hp == 90

    unit1.addHitPoints(40)
    assert unit1.hp == 100


def test_attack():
    unit1 = Unit('SoLdIeR', 100, 100, 10)
    unit2 = Unit('SoLdIeR', 100, 100, 10)
    assert unit1.hp == 100
    assert unit2.hp == 100
    unit1.attack(unit2)
    assert unit1.hp == 95
    assert unit2.hp == 90


def test_unit_attack_exception():
    soldier = Unit('Soldier', 10, 10, 20)
    warrior = Unit('Warrior', 10, 10, 20)

    with pytest.raises(UnitIsDeadException):
        soldier.attack(warrior)

    with pytest.raises(UnitIsDeadException):
        soldier.counterAttack(warrior)

    with pytest.raises(UnitIsDeadException):
        soldier.takeDamage(warrior.dmg)


def test_damage_greater_than_hp():
    soldier = Unit('Soldier', 20, 20, 20)

    soldier.takeDamage(20)
    assert soldier.hp == 0


def test_unit_to_string():
    soldier = Unit('Soldier', 100, 100, 20)

    assert str(soldier) == 'Soldier: (100/100), dmg: 20'


def test_counter_attack_exception():
    unit1 = Unit('SoLdIeR', 100, 100, 50)
    unit2 = Unit('SoLdIeR', 100, 100, 210)
    with pytest.raises(UnitIsDeadException):
        unit1.attack(unit2)


def test_unit_constructor():
    soldier = Unit('Soldier', 100, 100, 20)

    assert soldier.name == 'Soldier'
    assert soldier.hp == 100
    assert soldier.maxHP == 100
    assert soldier.dmg == 20


def test_unit_setters():
    soldier = Unit('SoLdIeR', 100, 100, 20)
    assert soldier.hp == 100

    soldier.hp = 50
    assert soldier.hp == 50

    soldier.hp += 50
    assert soldier.hp == 100

    soldier.maxHP -= 90
    assert soldier.maxHP == 10

    with pytest.raises(ValueError):
        soldier.hp = -100

    with pytest.raises(ValueError):
        soldier.hp -= 100

    soldier.dmg = 50
    assert soldier.dmg == 50

    soldier.name = 'Ivan'
    assert soldier.name == 'Ivan'

    # assert soldier.hp == 10


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
    ('error', ValueError),
    (dir, TypeError)
])
def test_check_numeric_exception(value, exception_type):
    with pytest.raises(exception_type):
        check_numeric(value)


@pytest.mark.parametrize('value2, exception_type2', [
    (-100, TypeError),
    ('error', TypeError),
    (dir, TypeError)
])
def test__check_type_exception(value2, exception_type2):
    soldier = Unit('SoLdIeR', 100, 100, 20)

    with pytest.raises(exception_type2):
        soldier.check_type(value2)

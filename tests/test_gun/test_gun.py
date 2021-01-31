import pytest

from gun.gun import prettify_string, check_numeric, Gun, WrongCapacity, NotReady, OutOfRounds


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


def test_gun_constructor():
    beretta = Gun(8, 'beretta')

    assert beretta.model == 'Beretta'
    assert beretta.amount == 0
    assert beretta.capacity == 8
    assert not beretta.is_ready
    assert beretta.amount == 0


def test_gun_setters():
    beretta = Gun(8, 'beretta')

    beretta.amount = 2
    assert beretta.amount == 2

    beretta.model = 'beretta-2'
    assert beretta.model == 'Beretta-2'

    beretta.capacity = 9
    assert beretta.capacity == 9

    beretta.is_ready = True
    assert beretta.is_ready

    beretta.amount = 3
    assert beretta.amount == 3


def test_setter_exception():
    kalash = Gun(100, 'kalash')
    kalash.amount = 90
    with pytest.raises(WrongCapacity):
        kalash.capacity = 10

    with pytest.raises(WrongCapacity):
        kalash.amount = 1000


def test_gun_to_string():
    kalash = Gun(100, 'kalash')

    assert str(kalash) == 'Kalash: capacity - 100, prepared - False, total shots - 0, amount - 0'


def test_prepare():
    kalash = Gun(100, 'kalash')
    kalash.prepare()

    assert kalash.is_ready


def test_reload():
    kalash = Gun(100, 'kalash')
    kalash.reload()

    assert kalash.amount == kalash.capacity


def test_shoot():
    kalash = Gun(100, 'kalash')
    kalash.reload()
    kalash.prepare()
    kalash.shoot()

    assert kalash.is_ready
    assert kalash.total_shots == 1
    assert kalash.amount == 99


def test_shoot_not_ready_exception():
    kalash = Gun(100, 'kalash')
    kalash.reload()
    with pytest.raises(NotReady):
        kalash.shoot()


def test_shoot_out_of_rounds_exception():
    kalash = Gun(1, 'kalash')
    kalash.reload()
    kalash.prepare()
    kalash.shoot()
    with pytest.raises(OutOfRounds):
        kalash.shoot()

from typing import Any

def prettify_string(value: str) -> str:
    if not isinstance(value, str):
        raise TypeError(f'value should be of type str: {value}')

    value = value.strip().lower()
    value = value.capitalize()
    return value


def check_numeric(value: int):
    value = int(value)
    if value <= 0:
        raise ValueError(f'value should be positive, got {value} instead')
    return value


class UnitIsDeadException(Exception):
    pass


class Unit:
    def __init__(self, name: str, hp: int, maxHP: int, dmg: int) -> None:
        self._name = prettify_string(name)
        self._hp = check_numeric(hp)
        self._maxHP = check_numeric(maxHP)
        self._dmg = check_numeric(dmg)

    @property
    def name(self) -> str:
        return self._name

    @property
    def hp(self) -> int:
        return self._hp

    @property
    def maxHP(self) -> int:
        return self._maxHP

    @property
    def dmg(self) -> int:
        return self._dmg

    @hp.setter
    def hp(self, value) -> None:
        self._hp = check_numeric(value)

    @maxHP.setter
    def maxHP(self, value) -> None:
        self._maxHP = check_numeric(value)

    @dmg.setter
    def dmg(self, value) -> None:
        self._dmg = check_numeric(value)

    @name.setter
    def name(self, value) -> None:
        self._name = prettify_string(value)

    def __str__(self) -> str:
        return f'{self.name}: ({self.hp}/{self.maxHP})'

    def __ensure_is_alive(self):
        if self.hp == 0:
            raise UnitIsDeadException()

    def takeDamage(self, damage_points) -> None:
        self.__ensure_is_alive()
        self._hp = self._hp - damage_points
        if self._hp < 0:
            self._hp = 0

    def addHitPoints(self, extra_hp) -> None:
        self.__ensure_is_alive()
        self._hp = self.hp + extra_hp
        if self._hp > self._maxHP:
            self._hp == self._maxHP

    def __check_type(self, enemy: Any) -> None:
        if not isinstance(enemy, self.__class__):
            raise TypeError(f'enemy param should be of type {self.__class__.__name__}')


    def attack(self, enemy: Any) -> None:
        self.__ensure_is_alive()
        self.__check_type(enemy)
        enemy.takeDamage(self._dmg)
        enemy.__ensure_is_alive()
        enemy.counterAttack(self)

    def counterAttack(self, enemy: Any) -> None:
        counter_dmg = self._dmg / 2
        if counter_dmg >= enemy._hp:
            enemy._hp = 0
        else:
            enemy._hp = enemy._hp - counter_dmg



if __name__ == '__main__':  # pragma: no cover
    unit1 = Unit('SoLdIeR', 100, 100, 10)
    print(unit1)
    # Unit.takeDamage(unit1, 40)
    # print(unit1)
    # Unit.addHitPoints(unit1, 10)
    # print(unit1)

    unit2 = Unit('Soldier2', 100, 100, 10)
    print(unit2)
    unit2.attack(unit1)
    print(unit1)
    print(unit2)


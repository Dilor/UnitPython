def prettify_string(value: str) -> str:
    if not isinstance(value, str):
        raise TypeError(f'value should be of type str: {value}')

    value = value.strip().lower()
    value = value.capitalize()
    return value


def check_numeric(value: int):
    value = int(value)
    if value < 0:
        raise ValueError(f'value should be positive, got {value} instead')
    return value


class WrongCapacity(Exception):
    pass


class NotReady(Exception):
    pass


class OutOfRounds(Exception):
    pass


class Gun:
    def __init__(self, capacity: int, model: str) -> None:
        self._amount = 0
        self._capacity = check_numeric(capacity)
        self._is_ready: bool = False
        self._model = prettify_string(model)
        self._total_shots = 0

    @property
    def amount(self) -> int:
        return self._amount

    @property
    def capacity(self) -> int:
        return self._capacity

    @property
    def is_ready(self) -> bool:
        return self._is_ready

    @property
    def model(self) -> str:
        return self._model

    @property
    def total_shots(self) -> int:
        return self._total_shots

    @amount.setter
    def amount(self, value) -> None:
        if value > self.capacity:
            raise WrongCapacity()
        self._amount = check_numeric(value)

    @capacity.setter
    def capacity(self, value) -> None:
        if value < self.amount:
            raise WrongCapacity()
        self._capacity = check_numeric(value)

    @is_ready.setter
    def is_ready(self, value) -> None:
        self._is_ready = value

    @model.setter
    def model(self, value) -> None:
        self._model = prettify_string(value)

    @total_shots.setter
    def total_shots(self, value) -> None:
        self._total_shots = value

    def __str__(self) -> str:
        return f'{self.model}: capacity - {self.capacity}, ' \
               f'prepared - {self.is_ready}, ' \
               f'total shots - {self.total_shots}, ' \
               f'amount - {self.amount}'

    def prepare(self) -> None:
        self.is_ready = not self.is_ready

    def reload(self):
        self.amount = self.capacity

    def shoot(self):
        if not self.is_ready:
            raise NotReady()
        if self.amount == 0:
            raise OutOfRounds()
        print("Bang!")
        self.amount -= 1
        self.total_shots += 1


if __name__ == '__main__':  # pragma: no cover
    kalash = Gun(100, 'kalash')
    print(kalash)
    kalash.reload()
    kalash.prepare()
    kalash.shoot()
    print(kalash)

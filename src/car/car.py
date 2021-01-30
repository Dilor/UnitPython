from point.point import Point


def prettify_string(value: str) -> str:
    if not isinstance(value, str):
        raise TypeError(f'value should be of type str: {value}')

    value = value.strip().lower()
    value = value.capitalize()
    return value


def check_numbers(value: int):
    value = int(value)
    if value < 0:
        raise ValueError(f'value should be >= 0')
    return value


class OutOfFuel(Exception):
    pass


class ToMuchFuel(Exception):
    pass


class Car:
    def __init__(self, fuel_amount: int,
                 fuel_capacity: int,
                 fuel_consumption: int,
                 location: Point,
                 model: str) -> None:
        self._fuel_amount = fuel_amount
        self._fuel_capacity = fuel_capacity
        self._fuel_consumption = fuel_consumption
        self._location = location
        self._model = prettify_string(model)

    @property
    def fuel_amount(self) -> int:
        return self._fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, value: int) -> None:
        self._fuel_amount = int(value)

    @property
    def fuel_capacity(self) -> int:
        return self._fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, value: int) -> None:
        self._fuel_capacity = int(value)

    @property
    def fuel_consumption(self) -> int:
        return self._fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, value: int) -> None:
        self._fuel_consumption = int(value)

    @property
    def location(self) -> Point:
        return self._location

    @location.setter
    def location(self, value: Point) -> None:
        self._location = value

    @property
    def model(self) -> str:
        return self._model

    @model.setter
    def model(self, value: str) -> None:
        self._model = str(value)

    def __str__(self) -> str:
        return f'{self.model}: fuel - {self.fuel_amount}/{self.fuel_capacity}, ' \
               f'consumption - {self.fuel_consumption}, location - {self.location}'

    def refill(self, fuel: int) -> None:
        if self.fuel_amount + fuel > self.fuel_capacity:
            raise ToMuchFuel('to much fuel')
        else:
            self.fuel_amount += fuel

    def drive(self, destination: Point) -> None:
        distance: float = destination.distance(self.location)
        fuel_needed: float = distance * self.fuel_consumption
        if fuel_needed > self.fuel_amount:
            raise OutOfFuel
        self.location = destination
        self.fuel_amount -= fuel_needed








if __name__ == '__main__':  # pragma: no cover
    point = Point(4, 4)
    point2 = Point(6, 6)
    car = Car(30, 90, 10, point, "MAzda")
    print(car)
    print(point)
    car.refill(20)
    print(car)
    car.drive(point2)
    print(car)




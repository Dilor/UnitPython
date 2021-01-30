from paper.paper import Paper


class OutOfInk(Exception):
    pass


def check_numeric(value: int):
    value = int(value)
    if value <= 0:
        raise ValueError(f'value should be positive, got {value} instead')
    return value


class Pen:
    def __init__(self, ink_capacity: int) -> None:
        self._ink_capacity = check_numeric(ink_capacity)
        self._ink_amount: int = ink_capacity

    @property
    def ink_capacity(self) -> int:
        return self._ink_capacity

    @property
    def ink_amount(self) -> int:
        return self._ink_amount

    @ink_capacity.setter
    def ink_capacity(self, value: int) -> None:
        self._ink_capacity = int(value)

    @ink_amount.setter
    def ink_amount(self, value: int) -> None:
        self._ink_amount = int(value)

    def write(self, paper: Paper, text: str) -> None:
        if self._ink_amount == 0:
            raise OutOfInk()
        if len(text) > self._ink_amount:
            paper.add_content(text[0: self.ink_amount])
            self.ink_amount = 0
        else:
            paper.add_content(text)
            self.ink_amount -= len(text)








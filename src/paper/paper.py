def check_numeric(value: int):
    value = int(value)
    if value <= 0:
        raise ValueError(f'value should be positive, got {value} instead')
    return value


class OutOfSpace(Exception):
    pass


class Paper:
    def __init__(self, max_symbols: int) -> None:
        self._max_symbols = check_numeric(max_symbols)
        self._content: str = ''
        self._symbols: int = 0

    @property
    def max_symbols(self) -> int:
        return self._max_symbols

    @property
    def content(self) -> str:
        return self._content

    @property
    def symbols(self) -> int:
        return self._symbols

    @max_symbols.setter
    def max_symbols(self, value) -> None:
        self._max_symbols = check_numeric(value)

    @content.setter
    def content(self, value) -> None:
        self._content = value

    @symbols.setter
    def symbols(self, value) -> None:
        self._symbols = check_numeric(value)

    def __str__(self) -> str:
        return f'Paper: max symbols - {self.max_symbols}, symbols - {self.symbols}'

    def add_content(self, value: str) -> None:
        total: int = len(value) + len(self.content)
        content_len: int = len(self.content)

        # if len(self.content) == self.max_symbols:
        #     raise OutOfSpace()
        if total >= self.max_symbols:
            # print(1)
            self.content += value[0:(self.max_symbols - content_len)]
            self.symbols = self.max_symbols
            raise OutOfSpace()
        else:
            self.content += value
            self.symbols += len(value)

    def show(self) -> None:
        print(self.content)

# if __name__ == '__main__':  # pragma: no cover
    # a4 = Paper(2000)
    # print(a4)
    # a4.add_content('some')
    # print(a4)
    # a4.show()
    # a4.add_content('thing')
    # a4.show()
    # a6 = Paper(3)
    # a6.add_content('test')

from collections.abc import Sequence
from typing import Any


class MyList(Sequence):
    def __init__(self) -> None:
        self._data = {}
        self._index = 0
        self._next_index = 0

    def append(self, value: str):
        for i in value.split():
            self._data[self._index] = i
            self._index += 1

    @property
    def view(self) -> dict:
        return self._data

    def __len__(self) -> int:
        return self._index

    def __getitem__(self, index: int) -> dict:
        return self._data[index]

    def __setitem__(self, index: int, value: Any):
        self._data[index] = value

    def __iter__(self):
        return self

    def __next__(self) -> dict:
        if self._next_index >= self._index:
            self._next_index = 0
            raise StopIteration
        value = self._data[self._next_index]
        self._next_index += 1

        return value


if __name__ == '__main__':
    ml = MyList()
    ml.append('Valorzinho Teste Macaco Daviz')
    ml[2] = 'Leão'
    # print(ml.view)
    # print(len(ml))
    for i in ml:
        print(i)
    print('-'*15)
    for i in ml:
        print(i)

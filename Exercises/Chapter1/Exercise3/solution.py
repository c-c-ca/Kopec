from typing import TypeVar, Generic, List
T = TypeVar('T')


class Stack(Generic[T]):

    def __init__(self) -> None:
        self._container: List[T] = []

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()

    def __repr__(self) -> str:
        return repr(self._container)


num_discs: int = 10
num_towers: int = 5
towers: List[Stack[int]] = [Stack() for _ in range(num_towers)]
for i in range(1, num_discs + 1):
    towers[0].push(i)


def hanoi_n(n: int, begin: Stack[int], end: Stack[int], *towers: Stack[int]) -> None:
    if n <= len(towers):
        for i in range(1, n):
            towers[i].push(begin.pop())
        end.push(begin.pop())
        for i in range(1, n):
            end.push(towers[n-i].pop())
    else:
        hanoi_n(n - len(towers), begin, towers[0], end, *towers[1:])
        hanoi_n(len(towers), begin, end, *towers)
        hanoi_n(n - len(towers), towers[0], end, begin, *towers[1:])


if __name__ == "__main__":
    hanoi_n(num_discs, towers[0], towers[-1], *towers[1:-1])
    for tower in towers:
        print(tower)
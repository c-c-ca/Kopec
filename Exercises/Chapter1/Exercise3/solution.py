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


num_discs: int = 15
num_steps: int = 0
tower_a: Stack[int] = Stack()
tower_b: Stack[int] = Stack()
tower_c: Stack[int] = Stack()
for i in range(1, num_discs + 1):
    tower_a.push(i)


def hanoi(begin: Stack[int], end: Stack[int], temp: Stack[int], n: int) -> None:
    global num_steps
    if n == 1:
        end.push(begin.pop())
        num_steps += 1
    else:
        hanoi(begin, temp, end, n - 1)
        hanoi(begin, end, temp, 1)
        hanoi(temp, end, begin, n - 1)


num_towers: int = 6
num_steps2: int = 0
towers: List[Stack[int]] = [Stack() for _ in range(num_towers)]
for i in range(1, num_discs + 1):
    towers[0].push(i)


def hanoi2(n: int, begin: Stack[int], end: Stack[int], *towers: Stack[int]) -> None:
    global num_steps2
    if n <= len(towers):
        for i in range(1, n):
            towers[i].push(begin.pop())
            num_steps2 += 1
        end.push(begin.pop())
        num_steps2 += 1
        for i in range(1, n):
            end.push(towers[n-i].pop())
            num_steps2 += 1
    else:
        hanoi2(n - len(towers), begin, towers[0], end, *towers[1:])
        hanoi2(len(towers), begin, end, *towers)
        hanoi2(n - len(towers), towers[0], end, begin, *towers[1:])


if __name__ == "__main__":
    hanoi(tower_a, tower_c, tower_b, num_discs)
    print(tower_a)
    print(tower_b)
    print(tower_c)
    print("Steps for 3 towers:", num_steps)

    hanoi2(num_discs, towers[0], towers[-1], *towers[1:-1])
    for tower in towers:
        print(tower)
    print(f"Steps for {num_towers} towers:", num_steps2)

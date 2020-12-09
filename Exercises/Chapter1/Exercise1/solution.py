from collections.abc import Iterable, Iterator
from textwrap import dedent
import timeit

class Fib7(Iterable[int]):

    def __init__(self, n: int) -> None:
        self.n: int = n

    def __iter__(self) -> Iterator[int]:
        self.curr: int = 0
        self.last: int = 0
        self.next: int = 1
        return self

    def __next__(self) -> int:
        val: int

        if self.curr < 2:
            val = self.curr
        elif self.curr < self.n:
            self.last, self.next = self.next, self.last + self.next
            val = self.next
        else:
            raise StopIteration

        self.curr += 1
        return val


def fib_from_iter(it: Iterable):
    for i in it:
        pass
    return i


if __name__ == "__main__":
    n = 5
    number = 1000000
    # Measure functional implementations
    for i in range(2, 6):
        print(
            f"fib{i}({n}) -",
            timeit.timeit(
                f"fib{i}({n})",
                setup=f"from fib{i} import fib{i}",
                number=number
            )
        )

    # Measure Generator implementation
    print(
        f"fib6({n}) -", 
        timeit.timeit(
            f"fib_from_iter(fib6({n}))",
            setup=dedent("""
            from fib6 import fib6
            from __main__ import fib_from_iter
            """),
            number=number
        )
    )

    # Measure Iterator implementation
    print(
        f"Fib7({n}) -",
        timeit.timeit(
            f"fib_from_iter(Fib7({n}))",
            setup=dedent("""
            from __main__ import Fib7, fib_from_iter
            """),
            number=number
        )
    )
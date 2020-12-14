from timeit import timeit
from textwrap import dedent
from generic_search import linear_contains, binary_contains


if __name__ == "__main__":
    number: int = 100
    print(timeit(
        "linear_contains(l, n)", dedent("""
        from random import randint
        from generic_search import linear_contains
        size = 1000000
        l = list(range(size))
        n = randint(0, size-1)"""),
        number=number))

    print(timeit(
        "binary_contains(l, n)", dedent("""
        from random import randint
        from generic_search import binary_contains
        size = 1000000
        l = list(range(size))
        n = randint(0, size-1)"""),
        number=number))
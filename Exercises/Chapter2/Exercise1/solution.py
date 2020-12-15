from timeit import timeit
from textwrap import dedent
from generic_search import linear_contains, binary_contains


if __name__ == "__main__":
    for contains in linear_contains, binary_contains:
        print(f"{contains.__name__}:", timeit(dedent(f"""
        for i in numbers:
            {contains.__name__}(search_space, i)"""), dedent(f"""
        from random import seed, randint
        from generic_search import {contains.__name__}
        search_space = list(range(1000000))
        seed(0)
        numbers = [randint(0, len(search_space)*2) for _ in range(100)]"""),
        number=1))

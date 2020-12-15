from timeit import timeit
from textwrap import dedent
from generic_search import linear_contains, binary_contains


if __name__ == "__main__":
    for contains in linear_contains, binary_contains:
        print(f"{contains.__name__}:", timeit(dedent(f"""
        for _ in range(100):
            {contains.__name__}(search_space, randint(0, 10 ** 7))"""), dedent(f"""
        from random import seed, randint
        from generic_search import {contains.__name__}
        seed(0)
        search_space = list(range(10 ** 6))"""),
        number=1))

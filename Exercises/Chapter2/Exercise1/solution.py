from random import randint
from timeit import timeit
from textwrap import dedent
from typing import List
from generic_search import linear_contains, binary_contains


search_space: List[int] = list(range(1000000))
numbers: List[int] = [randint(0, len(search_space)*2) for _ in range(100)]


if __name__ == "__main__":
    for contains in linear_contains, binary_contains:
        print(f"{contains.__name__}:", timeit(dedent(f"""
        for i in numbers:
            {contains.__name__}(search_space, i)"""), dedent(f"""
        from __main__ import search_space, numbers
        from generic_search import {contains.__name__}"""),
        number=1))
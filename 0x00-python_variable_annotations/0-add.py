#!/usr/bin/env python3
"""type-annotated add function"""


def add(a: float, b: float) -> float:
    """type-annotated add function, adds 2 float numbers

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The sum of `a` and `b`.
    """
    return a + b

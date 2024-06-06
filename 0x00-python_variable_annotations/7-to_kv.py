#!/usr/bin/env python3
"""Type-annotated to_kv function"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Converts a string and a number to a tuple with the string and the square
        of the number.

    Args:
        k (str): The string.
        v (Union[int, float]): The number (either an int or a float).

    Returns:
        Tuple[str, float]: A tuple containing the string and the square of the
                            number as a float.
    """
    return (k, v ** 2)

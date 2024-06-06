#!/usr/bin/env python3
"""Type-annotated make_multiplier function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Create a multiplier function.

    Args:
        multiplier (float): The value by which the input will be multiplied.

    Returns:
        Callable[[float], float]: A function that takes a float input and
                returns the result of multiplying it by the given multiplier.
    """
    def m(num: float) -> float:
        """Multiplies a number by the specified multiplier.

        Args:
            num (float): The number to be multiplied.

        Returns:
            float: The result of multiplying the input by the multiplier.
        """
        return num * multiplier
    return m

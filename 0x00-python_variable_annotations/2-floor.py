#!/usr/bin/env python3
"""Type-annotated floor function"""
import math


def floor(n: float) -> int:
    """Calculate the floor of a float number.

    Args:
        n (float): A float number.

    Returns:
        int: The floor of the input float.
    """
    return math.floor(n)

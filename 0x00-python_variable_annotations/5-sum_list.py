#!/usr/bin/env python3
"""Type-annotated sum_list function"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Calculate the sum of a list of floats.

    Args:
        input_list (List[float]): A list of float numbers.

    Returns:
        float: The sum of the numbers in the input list.
    """
    return sum(input_list)

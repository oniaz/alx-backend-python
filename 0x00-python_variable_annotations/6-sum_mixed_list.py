#!/usr/bin/env python3
"""Type-annotated sum_mixed_list function"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Calculate the sum of a list of integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): A list of integers and floats.

    Returns:
        float: The sum of the numbers in the input list.
    """
    return sum(mxd_lst)

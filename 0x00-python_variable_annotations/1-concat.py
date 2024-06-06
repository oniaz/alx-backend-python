#!/usr/bin/env python3
"""type-annotated concat function"""


def concat(str1: str, str2: str) -> str:
    """type-annotated concat function, concatenates two strings

    Args:
        str1 (str): The first string.
        str1 (str): The second string.

    Returns:
        str: The concatenatination of `str1` and `str2`.
    """
    return str1 + str2

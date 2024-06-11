#!/usr/bin/env python3
"""Defines an asynchronous generator that yields random float numbers."""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Asynchronously generates a list of random float numbers.

    Returns:
        List[float]: A list of random float numbers.
    """
    return [value async for value in async_generator()]

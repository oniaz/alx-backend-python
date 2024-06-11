#!/usr/bin/env python3
"""Defines an asynchronous generator that yields random float numbers."""
import asyncio
import random
from typing import Generator

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[float, None, None]:
    """
    Asynchronously generates a list of random float numbers.

    Returns:
        Generator[float, None, None]:
                A generator yielding random float numbers.
    """
    return [value async for value in async_generator()]

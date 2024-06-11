#!/usr/bin/env python3
"""Defines an asynchronous generator that yields random float numbers."""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronously yields 10 random float numbers between 0 and 10.

    Args:
        None

    Returns:
        AsyncGenerator[float, None]:
            An asynchronous generator yielding random float numbers.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

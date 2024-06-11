#!/usr/bin/env python3
"""Execute async_comprehension four times in parallel using asyncio.gather and
    measure the time taken."""
import asyncio
from typing import List
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Execute async_comprehension four times in parallel using asyncio.gather and
    measure the time taken.

    Returns:
        float: The time taken for execution in seconds.
    """
    start_time = time.time()

    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    end_time = time.time()
    return end_time - start_time

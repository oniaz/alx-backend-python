#!/usr/bin/env python3
"""An asyncio-based module for asynchronously waiting for random durations
    of time."""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Calls wait_random n times concurrently with random delays up to
        max_delay.

    Args:
        n (int): The number of times to call wait_random.
        max_delay (int): The maximum delay time in seconds for wait_random.

    Returns:
        List[float]: A list of the delay times for each call to wait_random.
    """
    return await asyncio.gather(*[wait_random(max_delay) for _ in range(n)])

#!/usr/bin/env python3
"""An asyncio-based module for asynchronously waiting for random duration
of time."""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronously waits for a random amount of time.

    Args:
        max_delay (int, optional): The maximum delay time in seconds.
            Defaults to 10.

    Returns:
        float: The actual delay time in seconds.

    """
    delay_time = random.uniform(0, max_delay)
    await asyncio.sleep(delay_time)
    return delay_time

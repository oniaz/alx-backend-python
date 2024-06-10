#!/usr/bin/env python3
"""An asyncio-based module for creating tasks that wait for random durations
    of time and running them concurrently."""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Create and run asynchronous tasks that wait for random durations
        of time and return sorted results.

    Args:
        n (int): The number of asynchronous tasks to create and run
            concurrently.
        max_delay (int): The maximum delay time in seconds for each
            asynchronous task.

    Returns:
        List[float]: A sorted list of delay times for each asynchronous task.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return sorted(await asyncio.gather(*tasks))

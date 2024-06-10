#!/usr/bin/env python3
"""A module for measuring the average duration of running asynchronous
    coroutines concurrently.
"""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the average duration of running asynchronous coroutines
        concurrently.

    Args:
        n (int): The number of asynchronous coroutines to run concurrently.
        max_delay (int): The maximum delay time in seconds for each coroutine.

    Returns:
        float: The average duration in seconds of running the coroutines.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    duration = end_time - start_time
    average_duration = duration / n

    return average_duration

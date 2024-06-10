#!/usr/bin/env python3
"""A module for creating asyncio tasks that wait for random durations of time.
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Create an asyncio task that waits for a random duration of time.

    Args:
        max_delay (int): The maximum delay time in seconds for the asynchronous
        task.

    Returns:
        asyncio.Task: An asyncio task that waits for a random duration of time.
    """
    return asyncio.create_task(wait_random(max_delay))

#!/usr/bin/env python3
"""This module contains a coroutine that runs multiple coroutines concurrently."""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times and return the delays in ascending order."""
    coroutines = [wait_random(max_delay) for _ in range(n)]
    delays = []

    for task in asyncio.as_completed(coroutines):
        delay = await task
        delays.append(delay)

    return delays

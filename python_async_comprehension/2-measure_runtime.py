#!/usr/bin/env python3
"""Module that defines the measure_runtime coroutine."""

import asyncio
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure the total runtime of four parallel async comprehensions."""
    start = time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end = time()
    return end - start

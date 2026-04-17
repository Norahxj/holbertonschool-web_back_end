#!/usr/bin/env python3
"""This module contains a coroutine that waits for a random delay."""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random delay, then return the delay value."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

#!/usr/bin/env python3

"""Modules implements asyncio"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Function returns an integer after a delay"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

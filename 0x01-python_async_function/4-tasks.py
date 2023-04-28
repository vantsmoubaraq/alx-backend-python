#!/usr/bin/env python3

"""Implement asynchronous function"""

from typing import List
wait_n = __import__("1-concurrent_coroutines").wait_n


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Return a list of delays"""
    wait = await wait_n(n, max_delay)
    return wait

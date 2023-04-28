#!/usr/bin/env python3

"""Module implement asynchoronous functions"""

from typing import List
import asyncio
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Returns an list of all delays"""
    tasks = []
    all_delays = []
    for i in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)
    for task in asyncio.as_completed(tasks):
        all_delays.append(await task)
    return all_delays

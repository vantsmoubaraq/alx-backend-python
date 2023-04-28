#!/usr/bin/env python3

"""Module returns average time of execution of all asynchronous operations"""

import asyncio
from time import perf_counter
wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Returns average time of execution"""
    start = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = perf_counter()
    return (end - start)

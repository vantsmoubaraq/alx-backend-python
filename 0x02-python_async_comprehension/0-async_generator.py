#!/usr/bin/env python3

"""yield a random number between 0 and 10 asynchronously"""

import asyncio
import random
import typing


async def async_generator() -> typing.Generator[float]:
    """yield a random number between 0 and 10 asynchronously"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

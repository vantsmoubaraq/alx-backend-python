#!/usr/bin/env python3

"""return the 10 random numbers"""

from typing import List
async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """return the 10 random numbers"""
    return [num async for num in async_generator()]

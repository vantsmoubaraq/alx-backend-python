#!/usr/bin/env python3

"""return the 10 random numbers"""

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension():
    """return the 10 random numbers"""
    return [num async for num in async_generator()]

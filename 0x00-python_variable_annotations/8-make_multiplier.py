#!/usr/bin/python3

"""Module takes a float and returns a function that multplies with another"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Multiplies any float by multiplier, returns a function"""

    return lambda any_float: multiplier * any_float

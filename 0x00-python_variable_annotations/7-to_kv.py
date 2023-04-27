#!/usr/bin/python3

"""Module returns a tuple from string and int or float"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Function returns a tuple"""
    return (k, float(v ** 2))

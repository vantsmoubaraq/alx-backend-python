#!/usr/bin/env python3

"""Modules computes sum of floats and int and returns float"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Function returns sum"""
    return float(sum(mxd_lst))

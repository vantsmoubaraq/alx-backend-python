#!/usr/bin/env python3

"""Returns first element in a dictionary or None"""

from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default:
                     Union[T, None] = None) -> Union[Any, T]:
    """Returns first element in a dictionary"""
    if key in dct:
        return dct[key]
    else:
        return default

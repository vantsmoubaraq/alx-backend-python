#!/usr/bin/env python3

from typing import Tuple, Any, List, Union, Optional

"""Returns a tuple multiplied by a factor"""


def zoom_array(lst: List[Any], factor: Union[int, float] = 2) -> List[Any]:
    """Returns a tuple multiplied by a factor"""
    zoomed_in: List[Any] = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)

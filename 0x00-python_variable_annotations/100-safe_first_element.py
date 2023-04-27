#!/usr/bin/env python3

"""Returns first elements of the list or None"""

from typing import Union, List, Sequence, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """Returns first elements of the list or None"""
    if lst:
        return lst[0]
    else:
        return None

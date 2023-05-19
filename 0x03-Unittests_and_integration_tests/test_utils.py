#!/usr/bin/env python3

"""
Module implements unit test
"""

import unittest
from parameterized import parameterized, parameterized_class
import requests
from typing import Dict, Union, Tuple
access_nested_map = __import__("utils").access_nested_map
get_json = __import__("utils").get_json


class TestAccessNestedMap(unittest.TestCase):
    """class implements unittest for TestAccessNestedMap"""

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(self, nested_map: Dict,
                               path: Tuple, expected: Union[int, str]):
        """Tests access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

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

    @parameterized.expand(
        [
            ({}, ("a",)),
            ({"a": 1}, ("a", "b")),
        ]
    )
    def test_access_nested_map_exception(self, nested_map: Dict,
                                         path: Tuple):
        """Tests raise of keyError exception"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Class tests utils.get_json"""

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    @unittest.mock.patch("requests.get")
    def test_get_json(self, test_url: str, expected: Dict,
                      mock_get: unittest.mock.Mock):
        """tests get_json"""

        mock_get.return_value.json.return_value = expected
        result = get_json(test_url)

        self.assertEqual(result, expected)
        mock_get.assert_called_once_with(test_url)

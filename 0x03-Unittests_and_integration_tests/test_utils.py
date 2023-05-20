#!/usr/bin/env python3

"""
Module implements unit test
"""

from unittest import TestCase, mock
from unittest.mock import patch, Mock
from parameterized import parameterized, parameterized_class
from typing import Dict, Union, Tuple
access_nested_map = __import__("utils").access_nested_map
get_json = __import__("utils").get_json
memoize = __import__("utils").memoize


class TestAccessNestedMap(TestCase):
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


class TestGetJson(TestCase):
    """Class tests utils.get_json"""

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    def test_get_json(self, test_url: str, expected: Dict):
        """tests get_json"""
        mock_get = Mock()
        mock_get.json.return_value = expected

        with patch("requests.get", return_value=mock_get) as mock_request:
            result = get_json(test_url)
            self.assertEqual(result, expected)
            mock_request.assert_called_once()


class TestMemoize(TestCase):
    """Class tests memoize function"""

    @parameterized.expand([
        (42),
        (42),
    ])
    def test_memoize(self, expected):
        """Tests memoize function"""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, "a_method",
                          return_value=expected) as mock_method:
            test_class = TestClass()
            result = test_class.a_property
            result = test_class.a_property
            self.assertEqual(result, expected)
            mock_method.assert_called_once()

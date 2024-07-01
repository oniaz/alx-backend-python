#!/usr/bin/env python3
"""
0x03. Unittests and Integration Tests
"""

import unittest
from typing import Any, Dict, Tuple
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    Tests for access_nested_map function
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self, nested_map: Dict, path: Tuple, expected: Any) -> None:
        """
        Test access_nested_map with various nested map and path combinations
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "'a'"),
        ({"a": 1}, ("a", "b"), "'b'")
    ])
    def test_access_nested_map_exception(
            self, nested_map: Dict, path: Tuple, exception_msg: str) -> None:
        """
        Test access_nested_map raises KeyError with the expected exception
        message
        """
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception), exception_msg)


if __name__ == '__main__':
    unittest.main()

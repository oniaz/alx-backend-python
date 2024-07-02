#!/usr/bin/env python3
"""
0x03. Unittests and Integration Tests
"""

import unittest
from typing import Any, Dict, Tuple, Callable
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize


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


class TestGetJson(unittest.TestCase):
    """
    Test the get_json function
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url: str, test_payload: Dict) -> None:
        """
        Test that get_json returns the expected result for different URLs and
        payloads.
        """

        with patch('requests.get') as mock_get:
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            result = get_json(test_url)

            mock_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """
    Test the memoize decorator function
    """
    def test_memoize(self) -> None:
        """
        Test that a_property is memoized
        """
        class TestClass:
            """ Test Class """
            def a_method(self):
                """ a method """
                return 42

            @memoize
            def a_property(self):
                """ a property """
                return self.a_method()

        with patch.object(
                TestClass, 'a_method', return_value=42) as mock_method:

            obj = TestClass()

            result1 = obj.a_property
            result2 = obj.a_property

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

            mock_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()

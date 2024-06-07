#!/usr/bin/env python3
"""Type-annotated safely_get_value function"""
from typing import Any, Mapping, TypeVar, Union


T = TypeVar('T')


def safely_get_value(
        dct: Mapping[Any, Any],
        key: Any,
        default: Union[T, None] = None
        ) -> Union[Any, T]:
    """Gets a value from a dictionary safely, returning a default if the key is
        not found.

    Args:
        dct (Mapping[Any, Any]): The dictionary from which to retrieve the
            value.
        key (Any): The key to look for in the dictionary.
        default (Union[T, None], optional): The default value to return if the
            key is not found. Defaults to None.

    Returns:
        Union[Any, T]: The value associated with the key if it exists,
            otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default

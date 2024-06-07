#!/usr/bin/env python3
"""Type-annotated safe_first_element function"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns the first element of the list if it exists, otherwise None.

    Args:
        lst (Sequence[Any]): A sequence of any elements.

    Returns:
        Union[Any, None]: The first element of the sequence if it exists,
                 otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None

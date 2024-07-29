"""Tests for random_dict package"""

from typing import Dict
import pytest
from random import randint
from random_dict import (
    random_bool_dict,
    random_float_dict,
    random_int_dict,
    random_string_dict,
    random_dict,
)


def compare_dictionaries(a: Dict, b: Dict):
    """Compare two dictionaries."""
    assert list(a.keys()) == list(b.keys())
    for k in a:
        assert isinstance(a[k], dict) == isinstance(b[k], dict)
        if isinstance(a[k], dict):
            compare_dictionaries(a[k], b[k])
        else:
            try:
                import numpy as np  # type: ignore

                if isinstance(a[k], np.ndarray):
                    assert np.all(a[k] == b[k])
                    continue
            except ImportError:
                pass

            try:
                import pandas as pd  # type: ignore

                if isinstance(a[k], pd.Series):
                    assert a[k].equals(b[k])
                    continue

                if isinstance(a[k], pd.DataFrame):
                    assert a[k].equals(b[k])
                    continue

            except ImportError:
                pass

            try:
                import polars as pl  # type: ignore

                if isinstance(a[k], pl.DataFrame):
                    assert a[k].equals(b[k])
                    continue

            except ImportError:
                pass

            assert a[k] == b[k]


def test_non_reproduceability():
    """Test random_dict."""
    for _ in range(100):
        for g in (
            random_bool_dict,
            random_float_dict,
            random_int_dict,
            random_string_dict,
            random_dict,
        ):
            a = g(randint(3, 15), randint(3, 15))
            b = g(randint(3, 15), randint(3, 15))
            error_was_not_raised = False
            try:
                compare_dictionaries(a, b)
                error_was_not_raised = True
            except AssertionError as exp:
                pass

            if error_was_not_raised:
                raise AssertionError(f"Failed for function={g.__name__}, a={a}, b={b}")


def test_reproduceability():
    """Test reproduceability."""
    for random_state in range(100):
        random_state += 5678
        for g in (
            random_bool_dict,
            random_float_dict,
            random_int_dict,
            random_string_dict,
            random_dict,
        ):
            max_depth = randint(2, 5)
            max_length = randint(2, 5)
            a = g(max_depth, max_length, random_state=random_state)
            b = g(max_depth, max_length, random_state=random_state)
            try:
                compare_dictionaries(a, b)
            except AssertionError as exp:
                raise AssertionError(
                    f"Failed for random_state={random_state}, max_depth={max_depth}, max_length={max_length}, "
                    f"function={g.__name__}, a={a}, b={b}"
                ) from exp

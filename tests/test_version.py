"""Checks that the version is correct."""

from validate_version_code import validate_version_code
from random_dict.__version__ import __version__


def test_version():
    """Checks that the version is correct."""
    assert validate_version_code(__version__)

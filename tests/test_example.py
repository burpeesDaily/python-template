"""Unit test example."""

from my_package import my_module
from my_package.sub_package import sub_module


def test_greet():
    """Test the greet function."""
    assert len(my_module.greet(name="John")) > 0


def test_square():
    """Test the square function."""
    assert sub_module.square(x=5) == 25

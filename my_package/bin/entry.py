"""Description about this module."""

import sys

from my_package import my_module


def main() -> None:
    """Entry for the project to be run as an executable."""
    try:
        print(my_module.greet(name=sys.argv[1]))
    except IndexError:
        print("Please input a name.")

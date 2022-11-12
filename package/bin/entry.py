"""Description about this module."""
import sys

from package import module


def main() -> None:
    """Entry for the project to be run as an executable."""
    try:
        print(module.greet(name=sys.argv[1]))
    except IndexError:
        print("Please input a name.")

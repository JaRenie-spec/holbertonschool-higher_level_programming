#!usr/bin/python3
"""Define a custom class 'MyList' that inherits from the built-in 'list' class
"""


class MyList(list):
    """a subclass of list that can print a sorted version of itself"""
    def print_sorted(self):
        """prints the list in sorted (ascendind) order."""
        print(sorted(self))

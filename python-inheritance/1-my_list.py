#!usr/bin/python3
"""Define a custom class 'MyList' that inherits from the built-in 'list' class
"""


class MyList(list):

    def print_sorted(self):
        print(sorted(self))

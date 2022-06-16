#!/usr/bin/env python3
from better_errors import Result


class MyClass:
    def __init__(self):
        pass

    def my_function(self, i: int) -> Result:
        if i >= 0:
            return Result(i, None)
        else:
            return Result(i, Exception("i is not greater than or equal to 0"))


if __name__ == "__main__":
    c = MyClass()

    # This shouldn't error
    i = c.my_function(1)
    if i.err is not None:
        print(f"an error occurred: {i.err}")
        quit(1)
    print(f"i == {i.ok}")

    # This should error
    i = c.my_function(-1)
    if i.err is not None:
        print(f"an error occurred: {i.err}")
        quit(1)
    print(f"i == {i.ok}")
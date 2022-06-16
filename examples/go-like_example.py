#!/usr/bin/env python3
from typing import Tuple, Any, Union


def my_function(i: int) -> Tuple[Any, Union[Exception, None]]:
    if i >= 0:
        return i, None
    else:
        return 0, Exception(f"{i} is not greater than or equal to 0")


if __name__ == "__main__":
    # This shouldn't error
    i, err = my_function(1)
    if err is not None:
        print(f"an error occurred: {err}")
        quit(1)
    print(f"i is {i}")

    # This should error
    i, err = my_function(-1)
    if err is not None:
        print(f"an error occurred: {err}")
        quit(1)
    print(f"i is {i}")
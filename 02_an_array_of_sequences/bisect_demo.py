import bisect
import sys
from typing import Union

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FORMAT = "{needle:2d} @ {position:2d}    {offset}{needle:<2d}"


def bisect_demo(bisect_function: Union[bisect.bisect, bisect.bisect_left]):
    for needle in reversed(NEEDLES):
        position = bisect_function(HAYSTACK, needle)
        offset = "  |" * position
        print(
            ROW_FORMAT.format(
                needle=needle,
                position=position,
                offset=offset,
            )
        )


if __name__ == "__main__":
    if sys.argv[-1] == "left":
        bisect_function = bisect.bisect_left
    else:
        bisect_function = bisect.bisect

    print(f"DEMO: {bisect_function.__name__}")
    print(f"haystack ->", " ".join(f"{number:2}" for number in HAYSTACK))
    bisect_demo(bisect_function)

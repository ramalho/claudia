import textwrap

# from fatbits import bitmap, pixelmap
from pprint import pprint

from src.fatbits import bitmap, WHITE, BLACK, pixelmap, pixelrow


def test_bitmap_2():
    expected = [
        [0, 1, 1, 1, 0],
        [1, 0, 0, 0, 1],
        [0, 0, 0, 0, 1],
        [0, 0, 1, 1, 0],
        [0, 1, 0, 0, 0],
        [1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1],
    ]
    assert expected == bitmap('2')


def test_pixelrow():
    mask = [0,0,1,0,0,0,0,0]
    result = pixelrow(mask)
    expected = [BLACK, BLACK, WHITE, BLACK, BLACK, BLACK, BLACK, BLACK]
    assert expected == result


def test_pixelmap():
    expected = [
        [BLACK, BLACK, WHITE, BLACK, BLACK, BLACK, BLACK, BLACK],
        [BLACK, WHITE, WHITE, BLACK, BLACK, BLACK, BLACK, BLACK],
        [BLACK, BLACK, WHITE, BLACK, BLACK, BLACK, BLACK, BLACK],
        [BLACK, BLACK, WHITE, BLACK, BLACK, BLACK, BLACK, BLACK],
        [BLACK, BLACK, WHITE, BLACK, BLACK, BLACK, BLACK, BLACK],
        [BLACK, BLACK, WHITE, BLACK, BLACK, BLACK, BLACK, BLACK],
        [BLACK, WHITE, WHITE, WHITE, BLACK, BLACK, BLACK, BLACK],
        [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK],
    ]
    result = pixelmap("1")
    assert expected == result

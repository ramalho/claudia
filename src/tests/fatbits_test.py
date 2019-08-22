import textwrap

# from fatbits import bitmap, pixelmap
from pprint import pprint

import pytest

from src.fatbits import bitmap, WHITE, BLACK, pixelmap, pixelrow, paint, RED


@pytest.fixture
def blank_canvas():
    return [
        [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK],
        [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK],
        [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK],
        [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK],
        [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK],
        [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK],
        [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK],
        [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK],
    ]


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
    mask = [0, 0, 1, 0, 0, 0, 0, 0]
    result = pixelrow(mask)
    expected = [BLACK, BLACK, WHITE, BLACK, BLACK, BLACK, BLACK, BLACK]
    assert expected == result


def test_pixelmap():
    expected = [
        [BLACK, BLACK, WHITE, BLACK, BLACK],
        [BLACK, WHITE, WHITE, BLACK, BLACK],
        [BLACK, BLACK, WHITE, BLACK, BLACK],
        [BLACK, BLACK, WHITE, BLACK, BLACK],
        [BLACK, BLACK, WHITE, BLACK, BLACK],
        [BLACK, BLACK, WHITE, BLACK, BLACK],
        [BLACK, WHITE, WHITE, WHITE, BLACK],
    ]
    result = pixelmap("1")
    assert expected == result


@pytest.mark.parametrize("row,col", [
    (-1, 1),
    (-1, -1),
    (1, -1),
    (8, 1),
    (8, 8),
    (1, 8),
])
def test_paint_invalid_anchor_asserted(blank_canvas, row, col):
    """
    Verify that every out of bounds top-left anchor position is asserted
    """
    little_canvas = [[BLACK]]
    with pytest.raises(AssertionError):
        paint(blank_canvas, little_canvas, row, col)


@pytest.mark.parametrize("row,col", [
    (2, 1),
    (2, 2),
    (1, 2),
])
def test_paint_clipping_asserted(blank_canvas, row, col):
    """
    Verify that every out of bounds top-left anchor position is asserted
    """
    pattern_7x7 = [
        [BLACK, WHITE, WHITE, BLACK, BLACK, BLACK, BLACK],
        [BLACK, BLACK, WHITE, BLACK, BLACK, BLACK, BLACK],
        [BLACK, BLACK, WHITE, BLACK, BLACK, BLACK, BLACK],
        [BLACK, BLACK, WHITE, BLACK, BLACK, BLACK, BLACK],
        [BLACK, BLACK, WHITE, BLACK, BLACK, BLACK, BLACK],
        [BLACK, WHITE, WHITE, WHITE, BLACK, BLACK, BLACK],
        [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK],
    ]
    with pytest.raises(AssertionError):
        paint(blank_canvas, pattern_7x7, row, col)


@pytest.mark.parametrize("row,col,expected", [
    (0, 0, [
        [RED, RED, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK],
        [RED, RED, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK],
        [RED, RED, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK],
        [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK],
        [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK],
        [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK],
        [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK],
        [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK],
    ]),
    (0, 6, [
        [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, RED, RED],
        [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, RED, RED],
        [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, RED, RED],
        [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK],
        [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK],
        [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK],
        [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK],
        [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK],
    ]),
    (5, 0, [
        [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK],
        [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK],
        [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK],
        [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK],
        [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK],
        [RED, RED, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK],
        [RED, RED, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK],
        [RED, RED, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK],
    ]),
    (5, 6, [
        [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK],
        [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK],
        [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK],
        [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK],
        [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK],
        [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, RED, RED],
        [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, RED, RED],
        [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, RED, RED],
    ]),
])
def test_paint(blank_canvas, row, col, expected):
    """
    Verify we can put the tiny red square in each corner of the canvas
    """
    pattern_3x2 = [
        [RED, RED],
        [RED, RED],
        [RED, RED],
    ]
    result = paint(blank_canvas, pattern_3x2, row, col)
    assert expected == result

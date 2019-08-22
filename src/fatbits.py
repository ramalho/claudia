#!/usr/bin/env python3
import copy
from pprint import pprint
from typing import NamedTuple, Tuple, List, Dict, Any

FONT_PBM_DATA = '''
P1
# Created by GIMP version 2.10.10 PNM plug-in
5 106
01110
10001
10011
10101
11001
10001
01110
00000
00000
00000
00000
00100
01100
00100
00100
00100
00100
01110
00000
00000
00000
00000
01110
10001
00001
00110
01000
10000
11111
00000
000000000000000111110000100010001100000110001011100000000000
0000000000000100011001010100101111100010000100000000000000000000011111
1000011110000010000110001011100000000000000000000000111010001000011110
1000110001011100000000000000000000011111000010001000100010000100001000
0000000000000000000001110100011000101110100011000101110000000000000000
0000001110100011000101111000010001011100
'''

CELL_HEIGHT = 11
GLYPH_HEIGHT = 7
GLYPH_WIDTH = 5


def load_font() -> Dict[str, List[List[int]]]:
    glyphs = {}
    pixels = ''.join(FONT_PBM_DATA.split('\n')[4:])
    for digit in range(10):
        octets = []
        for offset in range(GLYPH_HEIGHT):
            start = digit * CELL_HEIGHT * GLYPH_WIDTH + offset * GLYPH_WIDTH
            end = start + GLYPH_WIDTH
            octets.append([int(x) for x in pixels[start:end]])
        glyphs[str(digit)] = octets
    return glyphs


BitMapType = List[List[int]]
glyphs: Dict[str, BitMapType] = load_font()


def bitmap(char: str) -> BitMapType:
    """
    Note:
        * result is a 5x7 matrix that must be overlayed on a 8x8
        
    Returns::
    
        [[0, 0, 1, 0, 0],
         [0, 1, 1, 0, 0],
         [0, 0, 1, 0, 0],
         [0, 0, 1, 0, 0],
         [0, 0, 1, 0, 0],
         [0, 0, 1, 0, 0],
         [0, 1, 1, 1, 0]]
    """
    return glyphs[char]


class Color(NamedTuple):
    r: int
    g: int
    b: int
    
    def __repr__(self):
        return f"{self.r:02x}{self.g:02x}{self.b:02x}"


PixelMapType = List[List[Color]]
WHITE = Color(255, 255, 255)
RED = Color(255, 0, 0)
GREEN = Color(0, 255, 0)
BLACK = Color(0, 0, 0)


def paint(destination: PixelMapType, pattern: PixelMapType, row: int, col: int) -> PixelMapType:
    """
    Replace pixels at destination with pattern anchored at (row, col)
    and return the resulting pixelmap
    
    Notes:
        * row, col are zero based
        * destination is an 8x8 matrix
    """
    result = copy.copy(destination)
    pattern_width = len(pattern[0])
    pattern_height = len(pattern)

    # any row, col refs that are out of bounds are a programmer error
    assert 0 <= row < 8 and 0 <= col < 8, f"Row or col out of bounds: row={row}, col={col}"
    assert row + pattern_height <= 8, f"Pattern will be clipped, {row + pattern_height - 8} too many rows"
    assert col + pattern_width <= 8, f"Pattern will be clipped, {col + pattern_width - 8} too many cols"
    
    dest_row_index = row
    for line in pattern:
        result[dest_row_index][col:col + pattern_width] = line
        dest_row_index += 1
    
    return result

def pixelrow(mask: List[int]) -> List[Color]:
    """
    Notes:
        mask rows contain 5 elements, we return 8
    """
    return [WHITE if x else BLACK for x in mask]


def pixelmap(char: str) -> PixelMapType:
    mask = bitmap(char)
    return [pixelrow(x) for x in mask]


def colored_glyph(char: str) -> PixelMapType:
    mask = bitmap(char)
    return [pixelrow(x) for x in mask]


def colored_rect(width: int, height: int, color: Color) -> PixelMapType:
    return [[color] * width] * height

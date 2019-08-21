#!/usr/bin/env python3
from pprint import pprint
from typing import NamedTuple, Tuple, List, Dict

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


def load_font() -> Dict[str, bytes]:
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


glyphs = load_font()


def bitmap(char: str) -> List[List[int]]:
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


WHITE = Color(255, 255, 255)
RED = Color(255, 0, 0)
GREEN = Color(0, 255, 0)
BLACK = Color(0, 0, 0)


def pixelrow(mask: List[int]) -> List[Color]:
    """
    Notes:
        mask rows contain 5 elements, we return 8
    """
    return [WHITE if x else BLACK for x in mask] + [BLACK] * 3


def pixelmap(char: str) -> List[List[Tuple]]:
    mask = bitmap(char)
    return [pixelrow(x) for x in mask] + [[BLACK] *8]

from enum import Enum
from typing import NamedTuple, List

from src.fatbits import Color, pixelmap, PixelMapType, colored_glyph, colored_rect, BLACK, paint


class Role(str, Enum):
    Leader: str = "leader"
    Follower: str = "follower"
    Candidate: str = "candidate"


class State(NamedTuple):
    term: int
    role: Role


InitialState = State(term=1, role=Role.Follower)


class Display:
    
    def __init__(self, node_color: Color):
        self.node_color = node_color
        self.current_state: State = InitialState
    
    def display(self) -> PixelMapType:
        """
        Place visual elements on blank canvas
        """
        term = self._display_term()
        follower = self._display_follower()
        canvas = self._new_canvas()
        
        canvas = paint(canvas, term, 1, 0)
        return paint(canvas, follower, 0, 6)
    
    def _display_term(self):
        """
        Return a PixelMapType containing the election term.
        Size is always 5x7
        Caller has to place it properly on the canvas
        """
        return colored_glyph(str(self.current_state.term))
    
    def _display_follower(self):
        """
        """
        return colored_rect(2, 8, self.node_color)
    
    def _new_canvas(self):
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

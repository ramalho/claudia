from pprint import pprint

from src.display import Display, State, InitialState
from src.fatbits import RED, BLACK, WHITE


def test_constructor():
    this_nodes_color = RED
    d = Display(this_nodes_color)
    assert d.node_color == this_nodes_color
    assert d.current_state == InitialState


def test_display_term_number():
    """
    Terms occupy cols (0,4) and rows (1,7)
    """
    node_color = RED
    d = Display(node_color)
    result = d._display_term()
    expected = [
        [BLACK, BLACK, WHITE, BLACK, BLACK],
        [BLACK, WHITE, WHITE, BLACK, BLACK],
        [BLACK, BLACK, WHITE, BLACK, BLACK],
        [BLACK, BLACK, WHITE, BLACK, BLACK],
        [BLACK, BLACK, WHITE, BLACK, BLACK],
        [BLACK, BLACK, WHITE, BLACK, BLACK],
        [BLACK, WHITE, WHITE, WHITE, BLACK],
    ]
    assert result == expected


def test_display_follower_initial_state():
    """
    Follower occupies pixels (6,7) (right - most 2 cols)
    """
    node_color = RED
    d = Display(node_color)
    result = d._display_follower()
    expected = [
        [RED, RED],
        [RED, RED],
        [RED, RED],
        [RED, RED],
        [RED, RED],
        [RED, RED],
        [RED, RED],
        [RED, RED],
    ]
    assert expected == result


def test_display():
    node_color = RED
    d = Display(node_color)
    result = d.display()
    expected = [
        [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, RED, RED],
        [BLACK, BLACK, WHITE, BLACK, BLACK, BLACK, RED, RED],
        [BLACK, WHITE, WHITE, BLACK, BLACK, BLACK, RED, RED],
        [BLACK, BLACK, WHITE, BLACK, BLACK, BLACK, RED, RED],
        [BLACK, BLACK, WHITE, BLACK, BLACK, BLACK, RED, RED],
        [BLACK, BLACK, WHITE, BLACK, BLACK, BLACK, RED, RED],
        [BLACK, BLACK, WHITE, BLACK, BLACK, BLACK, RED, RED],
        [BLACK, WHITE, WHITE, WHITE, BLACK, BLACK, RED, RED],
    ]
    assert expected == result

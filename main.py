import curses

from curses_context import Curses_Context
from keyboard import KEYS, Keyboard
from scale import Scale


def main(window):

    # Create curses help functions
    cc = Curses_Context(curses, window)

    # Define color pairs
    cc.init_pair(KEYS.WHITE, curses.COLOR_BLACK, curses.COLOR_WHITE)
    cc.init_pair(KEYS.BLACK, curses.COLOR_WHITE, curses.COLOR_BLACK)

    s = Scale()
    k = Keyboard(cc, s)
    k.draw_keyboard(0, 0)
    window.getkey()


curses.wrapper(main)

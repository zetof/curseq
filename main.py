import curses

from keyboard import Keyboard

def main(window):
  curses.curs_set(0)
  k = Keyboard(window)
  k.draw_keyboard(0, 0)
  window.getkey()

# Start curses in wrapper mode
curses.wrapper(main)

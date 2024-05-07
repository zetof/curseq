import curses

from keyboard import Keyboard

def main(window):
  k = Keyboard(window)
  k.draw_keyboard(0, 0)
  window.getkey()

# Start curses in wrapper mode
curses.wrapper(main)

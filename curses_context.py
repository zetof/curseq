class Curses_Context:

  def __init__(self, curses, window):
    self.curses = curses
    self.window = window
    self.curses.curs_set(0)

  def init_pair(self, index, foreground, background):
    self.curses.init_pair(index, foreground, background)

  def get_pair(self, index):
    return self.curses.color_pair(index)

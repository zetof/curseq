class Curses_Context:

    def __init__(self, curses, window):
        self.curses = curses
        self.window = window
        self.curses.curs_set(0)
        window_size = window.getmaxyx()
        self.max_col = window_size[0] - 1
        self.max_line = window_size[1] - 1

    def init_pair(self, index, foreground, background):
        self.curses.init_pair(index, foreground, background)

    def get_pair(self, index):
        return self.curses.color_pair(index)

    def log_to_screen(self, value):
        self.window.addstr(self.max_col, 0, value)

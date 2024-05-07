class KEYS(object):

    WHITE = 6
    BLACK = 3
    SIDES = "    |"
    BOTTOM = "+---+"


class Keyboard:

    def __init__(self, curses_context, scale):
        self.cc = curses_context
        self.scale = scale

    def draw_key(self, line, col, key_type):
        for i in range(0, key_type):
            self.cc.window.addstr(line + i, col, KEYS.SIDES,
                                  self.cc.get_pair(key_type))
            # self.w.addstr(line + i +1, col, KEYS.BOTTOM, color)

    def draw_keyboard(self, line, col):
        for i in range(0, 32, 4):
            self.draw_key(line, col + i, KEYS.WHITE)
        for i in range(2, 10, 4):
            self.draw_key(line, col + i, KEYS.BLACK)
        for i in range(18, 30, 4):
            self.draw_key(line, col + i, KEYS.BLACK)

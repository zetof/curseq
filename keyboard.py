class KEYS(object):

    WHITE = 6
    BLACK = 3
    SIDES = "    |"
    BOTTOM = "+---+"


class Keyboard:

    def __init__(self, curses_context, scale):
        self.cc = curses_context
        self.scale = scale

    def draw_key(self, x, y, key_type):
        for i in range(0, key_type):
            self.cc.print_at(x, y + i, KEYS.SIDES, key_type)
            # self.w.addstr(line + i +1, col, KEYS.BOTTOM, color)

    def draw_keyboard(self, x, y):
        for i in range(0, 32, 4):
            self.draw_key(x + i, y, KEYS.WHITE)
        for i in range(2, 10, 4):
            self.draw_key(x + i, y, KEYS.BLACK)
        for i in range(18, 30, 4):
            self.draw_key(x + i, y, KEYS.BLACK)

class KEY_ELEMENTS(object):
  WHITE = 6
  BLACK = 3
  SIDES = "|   |"
  BOTTOM = "+---+"

class Keyboard:

  def __init__(self, window, key="C", scale="MAJOR", octave=4):
    self.w = window
    self.key = key
    self.scale = scale
    self.octave = octave

  def draw_key(self, line, col, key_type):
    for i in range(0, key_type):
      self.w.addstr(line + i, col, KEY_ELEMENTS.SIDES) 
    self.w.addstr(line + i +1, col, KEY_ELEMENTS.BOTTOM) 

  def draw_keyboard(self, line, col):
    for i in range(0, 32, 4):
      self.draw_key(line, col + i, KEY_ELEMENTS.WHITE)
    for i in range(2, 10, 4):
      self.draw_key(line, col + i, KEY_ELEMENTS.BLACK)
    for i in range(18, 30, 4):
      self.draw_key(line, col + i, KEY_ELEMENTS.BLACK)

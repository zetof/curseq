class DEGREES(object):
  DEFAULT_TONALITY = "C"
  DEFAULT_SCALE = "MAJOR"
  DEFAULT_OCTAVE = 5
  OCTAVE = 12
  OCTAVE_MIN = 2
  OCTAVE_MAX = 8
  ACCIDENTALS = [1, 3, 6, 8, 10]
  TONALITIES = {
    "C" : 0,
    "C#": 1,
    "Db": 1,
    "D":  2
  }
  SCALES = {
    "MAJOR": [0, 2, 4, 5, 7, 9, 11]
  }

  @classmethod
  def GET_TONALITY(cls, name):
    try:
      return cls.TONALITIES[name]
    except KeyError:
      return False

  @classmethod
  def GET_SCALE(cls, name):
    try:
      return cls.SCALES[name]
    except KeyError:
      return False

  @classmethod
  def GET_OCTAVE(cls, index):
    if index < cls.OCTAVE_MIN or index > cls.OCTAVE_MAX:
      return False
    else:
      return index


class Scale:

  def __init__(self, tonality=DEGREES.DEFAULT_TONALITY, scale=DEGREES.DEFAULT_SCALE, octave=DEGREES.DEFAULT_OCTAVE):
    self.set_tonality(tonality)
    self.set_scale(scale)
    self.set_octave(octave)
    self.to_string()

  def set_tonality(self, name):
    self.tonality = DEGREES.GET_TONALITY(name)

  def set_scale(self, name):
    self.scale = DEGREES.GET_SCALE(name)

  def set_octave(self, index):
    self.octave = DEGREES.GET_OCTAVE(index)

  def to_string(self):
    print("TONALITY: {}".format(self.tonality))

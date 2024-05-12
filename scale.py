class DEGREES(object):

    DEFAULT_TONALITY = "C"
    DEFAULT_SCALE = "MAJOR"
    DEFAULT_OCTAVE = 5
    OCTAVE_STEP = 12
    OCTAVE_MIN = 2
    OCTAVE_MAX = 8
    ACCIDENTALS = [1, 3, 6, 8, 10]
    TONALITIES = {
        "C": 0,
        "C#": 1,
        "Db": 1,
        "D": 2
    }
    SCALES = {
        "MAJOR": [0, 2, 4, 5, 7, 9, 11]
    }

    @classmethod
    def GET_TONALITY(cls, name):
        try:
            return name, cls.TONALITIES[name]
        except KeyError:
            return cls.DEFAULT_TONALITY, cls.TONALITIES[cls.DEFAULT_TONALITY]

    @classmethod
    def GET_SCALE(cls, name):
        try:
            return name, cls.SCALES[name]
        except KeyError:
            return cls.DEFAULT_SCALE, cls.SCALES[cls.DEFAULT_SCALE]

    @classmethod
    def GET_OCTAVE(cls, index):
        if index >= cls.OCTAVE_MIN and index <= cls.OCTAVE_MAX:
            return index
        else:
            return cls.DEFAULT_OCTAVE


class Scale:

    def __init__(self, tonality=DEGREES.DEFAULT_TONALITY,
                 scale=DEGREES.DEFAULT_SCALE,
                 octave=DEGREES.DEFAULT_OCTAVE):
        tonality = DEGREES.GET_TONALITY(tonality)
        self.tonality_name = tonality[0]
        self.tonality = tonality[1]
        scale = DEGREES.GET_SCALE(scale)
        self.scale_name = scale[0]
        self.scale = scale[1]
        self.octave = DEGREES.GET_OCTAVE(octave)
        self.degrees = self.build_degrees()

    def set_tonality(self, tonality):
        self.tonality = DEGREES.GET_TONALITY(tonality)

    def set_scale(self, scale):
        self.scale = DEGREES.GET_SCALE(scale)

    def set_octave(self, octave):
        self.octave = DEGREES.GET_OCTAVE(octave)

    def build_degrees(self):
        start = DEGREES.OCTAVE_STEP * self.octave
        current = start
        index = 0
        degrees = []
        while current - start < DEGREES.OCTAVE_STEP:
            shift = 0
            try:
                current = start + shift + self.scale[index]
            except IndexError:
                shift += DEGREES.OCTAVE_STEP
                index = 0
                current = start + shift + self.scale[index]
            index += 1
            degrees.append(current)

        return degrees

    def to_string(self):
        return "TONALITY: {} / SCALE: {} / OCTAVE: {} -> DEGREES: {}".format(
            self.tonality_name, self.scale_name, self.octave, self.degrees)

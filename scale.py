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
        "D": 2,
        "D#": 3,
        "Eb": 3,
        "E": 4,
        "F": 5,
        "F#": 6,
        "Gb": 6,
        "G": 7,
        "G#": 8,
        "Ab": 8,
        "A": 9,
        "A#": 10,
        "Bb": 10,
        "B": 11
    }
    SCALES = {
        "AEOLIAN": (0, 2, 3, 5, 7, 8, 10),
        "AHIRBHAIRAV": (0, 1, 4, 5, 7, 9, 10),
        "AUGMENTED": (0, 3, 4, 7, 8, 11),
        "AUGMENTED 2": (0, 1, 4, 5, 8, 9),
        "BARTOK": (0, 2, 4, 5, 7, 8, 10),
        "BHAIRAV": (0, 1, 4, 5, 7, 8, 11),
        "CHINESE": (0, 4, 6, 7, 11),
        "CHROMATIC": (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),
        "DIMINISHED": (0, 1, 3, 4, 6, 7, 9, 10),
        "DIMINISHED 2": (0, 2, 3, 5, 6, 8, 9, 11),
        "DORIAN": (0, 2, 3, 5, 7, 9, 10),
        "EGYPTIAN": (0, 2, 5, 7, 10),
        "ENIGMATIC": (0, 1, 4, 6, 8, 10, 11),
        "GONG": (0, 2, 4, 7, 9),
        "HARMONIC MAJOR": (0, 2, 4, 5, 7, 8, 11),
        "HARMONIC MINOR": (0, 2, 3, 5, 7, 8, 11),
        "HEX AEOLIAN": (0, 3, 5, 7, 8, 10),
        "HEX DORIAN": (0, 2, 3, 5, 7, 10),
        "HEX MAJOR 6": (0, 2, 4, 5, 7, 9),
        "HEX MAJOR 7": (0, 2, 4, 7, 9, 11),
        "HEX PHRYGIAN": (0, 1, 3, 5, 8, 10),
        "HEX SUS": (0, 2, 5, 7, 9, 10),
        "HINDU": (0, 2, 4, 5, 7, 8, 10),
        "HIRAJOSHI": (0, 2, 3, 7, 8),
        "HUNGARIAN MINOR": (0, 2, 3, 6, 7, 8, 11),
        "INDIAN": (0, 4, 5, 7, 10),
        "IONIAN": (0, 2, 4, 5, 7, 9, 11),
        "IWATO": (0, 1, 5, 6, 10),
        "JIAO": (0, 3, 5, 8, 10),
        "KUMAI": (0, 2, 3, 7, 9),
        "LEADING WHOLE TONE": (0, 2, 4, 6, 8, 10, 11),
        "LOCRIAN": (0, 1, 3, 5, 6, 8, 10),
        "LOCRIAN MAJOR": (0, 2, 4, 5, 6, 8, 10),
        "LYDIAN": (0, 2, 4, 6, 7, 9, 11),
        "LYDIAN MINOR": (0, 2, 4, 6, 7, 8, 10),
        "MAJOR": (0, 2, 4, 5, 7, 9, 11),
        "MAJOR PENTATONIC": (0, 2, 4, 7, 9),
        "MARVA": (0, 1, 4, 6, 7, 9, 11),
        "MELODIC MAJOR": (0, 2, 4, 5, 7, 8, 10),
        "MELODIC MINOR": (0, 2, 3, 5, 7, 9, 11),
        "MELODIC MINOR DESCENDING": (0, 2, 3, 5, 7, 8, 10),
        "NATURAL MINOR": (0, 2, 3, 5, 7, 8, 10),
        "MINOR PENTATONIC": (0, 3, 5, 7, 10),
        "MIXOLYDIAN": (0, 2, 4, 5, 7, 9, 10),
        "NEAPOLITAN MAJOR": (0, 1, 3, 5, 7, 9, 11),
        "NEAPOLITAN MINOR": (0, 1, 3, 5, 7, 8, 11),
        "PELOG": (0, 1, 3, 7, 8),
        "PHRYGIAN": (0, 1, 3, 5, 7, 8, 10),
        "PROMETHEUS": (0, 2, 4, 6, 11),
        "PURVI": (0, 1, 4, 6, 7, 8, 11),
        "RITUSEN": (0, 2, 5, 7, 9),
        "ROMANIAN MINOR": (0, 2, 3, 6, 7, 9, 10),
        "SCRIABIN": (0, 1, 4, 7, 9),
        "SHANG": (0, 2, 5, 7, 10),
        "SPANISH": (0, 1, 4, 5, 7, 8, 10),
        "SUPER LOCRIAN": (0, 1, 3, 4, 6, 8, 10),
        "TODI": (0, 1, 3, 6, 7, 8, 11),
        "WHOLE TONE": (0, 2, 4, 6, 8, 10),
        "YU": (0, 3, 5, 7, 10),
        "ZHI": (0, 2, 5, 7, 9)
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

    def get_tonality_name(self):
        return self.tonality_name

    def get_scale_name(self):
        return self.scale_name

    def get_octave(self):
        return self.octave

    def get_degrees(self):
        return self.degrees

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

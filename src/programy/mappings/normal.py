from programy.mappings.base import DoubleStringPatternSplitCollection

class NormalCollection(DoubleStringPatternSplitCollection):

    def __init__(self):
        DoubleStringPatternSplitCollection.__init__(self)

    def normalise(self, denormal):
        if self.has_key(denormal):
            return self.value(denormal)
        return None

    def normalise_string(self, string):
        return self.replace_by_pattern(string)

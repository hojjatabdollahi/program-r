from programr.mappings.base import DoubleStringPatternSplitCollection

class GenderCollection(DoubleStringPatternSplitCollection):

    def __init__(self):
        DoubleStringPatternSplitCollection.__init__(self)

    def gender(self, gender):
        if self.has_key(gender):
            return self.value(gender)
        return None

    def genderise_string(self, string):
        return self.replace_by_pattern(string)

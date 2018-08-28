from programy.mappings.base import DoubleStringPatternSplitCollection

class PersonCollection(DoubleStringPatternSplitCollection):

    def __init__(self):
        DoubleStringPatternSplitCollection.__init__(self)

    def person(self, gender):
        if self.has_key(gender):
            return self.value(gender)

    def personalise_string(self, string):
        return self.replace_by_pattern(string)

import re

from programr.dynamic.sets.set import DynamicSet


class IsRomanNumeral(DynamicSet):

    NAME = "ROMAN"

    def __init__(self, config):
        DynamicSet.__init__(self, config)

    def is_member(self, client_context, value):
        if value is not None:
            match = re.match("^[IVXMC]*$", value)
            return match is not None
        return False

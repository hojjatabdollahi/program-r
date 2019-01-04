from programr.dynamic.sets.set import DynamicSet


class IsNumeric(DynamicSet):

    NAME = "NUMBER"

    def __init__(self, config):
        DynamicSet.__init__(self, config)

    def is_member(self, client_context, value):
        if value is not None:
            return value.isnumeric()
        return False

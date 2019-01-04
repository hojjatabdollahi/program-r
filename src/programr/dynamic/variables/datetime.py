from programr.dynamic.variables.variable import DynamicVariable

from programr.utils.text.dateformat import DateFormatter


class GetTime(DynamicVariable):

    def __init__(self, config):
        DynamicVariable.__init__(self, config)

    def get_value(self, client_context, value=None):
        formatter = DateFormatter()
        return formatter.time_representation()

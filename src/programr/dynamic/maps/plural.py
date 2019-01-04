from programr.utils.logging.ylogger import YLogger

from programr.dynamic.maps.map import DynamicMap


class PluralMap(DynamicMap):

    NAME = "PLURAL"
    STATICS = {"MOUSE": "MICE"
              }

    def __init__(self, config):
        DynamicMap.__init__(self, config)

    def static_map(self, value):
        if value in PluralMap.STATICS:
            return PluralMap.STATICS[value]
        return None

    def map_value(self, client_context, input_value):
        plural_value = self.static_map(input_value)
        if plural_value is None:
            if input_value.endswith('Y'):
                plural_value = input_value[:-1] + 'IES'
            else:
                plural_value = input_value + "S"

        YLogger.debug(client_context, "PluralMap converted %s to %s", input_value, plural_value)
        return plural_value

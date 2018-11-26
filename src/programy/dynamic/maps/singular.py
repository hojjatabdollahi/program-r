from programy.utils.logging.ylogger import YLogger

from programy.dynamic.maps.map import DynamicMap


class SingularMap(DynamicMap):

    NAME = "SINGULAR"
    STATICS = {"MICE": "MOUSE"}

    def __init__(self, config):
        DynamicMap.__init__(self, config)

    @staticmethod
    def static_map(value):
        if value in SingularMap.STATICS:
            return SingularMap.STATICS[value]
        return None

    def map_value(self, client_context, input_value):
        singular_value = SingularMap.static_map(input_value)
        if singular_value is None:
            if input_value.endswith('IES'):
                singular_value = input_value[:-3] + "Y"
            elif input_value.endswith('S'):
                singular_value = input_value[:-1]
            else:
                singular_value = input_value

        YLogger.debug(client_context, "SingleMap converted %s to %s", input_value, singular_value)
        return singular_value

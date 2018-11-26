from programy.utils.logging.ylogger import YLogger

from programy.dynamic.maps.map import DynamicMap


class SuccessorMap(DynamicMap):

    NAME = "SUCCESSOR"

    def __init__(self, config):
        DynamicMap.__init__(self, config)

    def map_value(self, client_context, input_value):
        try:
            int_value = int(input_value)
            str_value = str(int_value + 1)
            YLogger.debug(client_context, "SuccessorMap converted %s to %s", input_value, str_value)
            return str_value
        except Exception:
            YLogger.error(client_context, "SuccessorMap could not convert %s to integer string", input_value)
            return ""

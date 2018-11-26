from programy.utils.logging.ylogger import YLogger
import xml.etree.ElementTree as ET

from programy.oob.oob import OutOfBandProcessor


class WifiOutOfBandProcessor(OutOfBandProcessor):
    """
    <oob>
        <wifi>on|off</wifi>
    </oob>
    """

    def __init__(self):
        OutOfBandProcessor.__init__(self)
        self._command = None

    def parse_oob_xml(self, oob: ET.Element):
        if oob is not None and oob.text is not None:
            self._command = oob.text
            return True
        else:
            YLogger.error(self, "Unvalid camera oob command - missing command")
            return False

    def execute_oob_command(self, client_context):
        YLogger.info(client_context, "WifiOutOfBandProcessor: Setting camera to=%s", self._command)
        return "WIFI"

from programy.utils.logging.ylogger import YLogger
import xml.etree.ElementTree as ET

from programy.oob.oob import OutOfBandProcessor


class DialOutOfBandProcessor(OutOfBandProcessor):
    """
    <oob>
        <dial>07777777777</dial>
    </oob>
    """

    def __init__(self):
        OutOfBandProcessor.__init__(self)
        self._number = None

    def parse_oob_xml(self, oob: ET.Element):
        if oob is not None and oob.text is not None:
            self._number = oob.text
            return True
        else:
            YLogger.error(self, "Unvalid dial oob command - missing dial text!")
            return False

    def execute_oob_command(self, client_context):
        YLogger.info(client_context, "DialOutOfBandProcessor: Dialing=%s", self._number)
        return "DIAL"

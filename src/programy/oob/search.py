from programy.utils.logging.ylogger import YLogger
import xml.etree.ElementTree as ET

from programy.oob.oob import OutOfBandProcessor


class SearchOutOfBandProcessor(OutOfBandProcessor):
    """
    <oob>
        <search>VIDEO <star/></search>
    </oob>
    """

    def __init__(self):
        OutOfBandProcessor.__init__(self)
        self._search = None

    def parse_oob_xml(self, oob: ET.Element):
        if oob is not None and oob.text is not None:
            self._search = oob.text
            return True
        else:
            YLogger.error(self, "Unvalid search oob command - missing search query!")
            return False

    def execute_oob_command(self, client_context):
        YLogger.info(client_context, "SearchOutOfBandProcessor: Searching=%s", self._search)
        return "SEARCH"

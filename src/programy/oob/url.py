from programy.utils.logging.ylogger import YLogger
import xml.etree.ElementTree as ET

from programy.oob.oob import OutOfBandProcessor


class URLOutOfBandProcessor(OutOfBandProcessor):
    """
    <oob>
        <url>http://<star/>.com</url>
    </oob>
    """
    def __init__(self):
        OutOfBandProcessor.__init__(self)
        self._url = None

    def parse_oob_xml(self, oob: ET.Element):
        if oob is not None and oob.text is not None:
            self._url = oob.text
            return True
        else:
            YLogger.error(self, "Unvalid url oob command - missing url!")
            return False

    def execute_oob_command(self, client_context):
        YLogger.info(client_context, "URLOutOfBandProcessor: Loading=%s", self._url)
        return "URL"

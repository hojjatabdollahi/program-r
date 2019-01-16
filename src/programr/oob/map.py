from programr.utils.logging.ylogger import YLogger
import xml.etree.ElementTree as ET

from programr.oob.oob import OutOfBandProcessor


class MapOutOfBandProcessor(OutOfBandProcessor):
    """
    <geooob>
        <map>Kinghorn</map>
    </geooob>
    """
    def __init__(self):
        OutOfBandProcessor.__init__(self)
        self._location = None

    def parse_oob_xml(self, oob: ET.Element):
        if oob is not None and oob.text is not None:
            self._location = oob.text
            return True
        else:
            YLogger.error(self, "Unvalid geomap oob command - missing location text!")
            return False

    def execute_oob_command(self, client_context):
        YLogger.info(client_context, "MapOutOfBandProcessor: Showing a map for location=%s", self._location)
        return "MAP"

from programr.oob.oob import OutOfBandProcessor
from programr.utils.logging.ylogger import YLogger
import xml.etree.ElementTree as ET
import json
import xmltodict

class RobotOutOfBandProcessor(OutOfBandProcessor):
    """
    <oob>
         <robot>
            <options>
                <option>yes</option>
                <option>no</option>
                <option>probably</option>
                <option>never</option>
            </options>
            <image>
                <filename>pic.jpg</filename>
                <duration>10</duration>
            </image>
            <video>
                <filename>f.mp4</filename>
            </video>
        </robot>
    </oob>

    """
    def __init__(self):
        OutOfBandProcessor.__init__(self)
        self._robot = {}

    def parse_oob_xml(self, oob: ET.Element):
        if oob is not None:
            oob_string = ET.tostring(oob, encoding='utf8', method='xml')
            self._robot = xmltodict.parse(oob_string, dict_constructor=dict)
            return True
        else:
            YLogger.error(self, "Unvalid geomap oob command - missing location text!")
            return False

    def execute_oob_command(self, client_context):
        YLogger.info(client_context, "OptionsOutOfBandProcessor: showing the options=%s", self._robot)
        return self._robot

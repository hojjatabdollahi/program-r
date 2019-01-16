from programr.utils.logging.ylogger import YLogger
import xml.etree.ElementTree as ET

from programr.oob.oob import OutOfBandProcessor


class ScheduleOutOfBandProcessor(OutOfBandProcessor):
    """
    <oob>
        <schedule><title><star/></title><description><lowercase><star index="2"/></lowercase></description><get name="sraix"/></schedule>
    </oob>
    """

    def __init__(self):
        OutOfBandProcessor.__init__(self)
        self._title = None
        self._description = None

    def parse_oob_xml(self, oob: ET.Element):
        if oob is not None:
            for child in oob:
                if child.tag == 'title':
                    self._title = child.text
                elif child.tag == 'description':
                    self._description = child.text
                else:
                    YLogger.error(self, "Unknown child element [%s] in schedule oob", child.tag)

            if self._title is not None and \
                self._description is not None:
                return True

        YLogger.error(self, "Invalid email schedule command")
        return False

    def execute_oob_command(self, client_context):
        YLogger.info(client_context, "ScheduleOutOfBandProcessor: Scheduling=%s", self._title)
        return "SCHEDULE"

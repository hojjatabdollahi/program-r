from programr.utils.logging.ylogger import YLogger
import xml.etree.ElementTree as ET

from programr.oob.oob import OutOfBandProcessor


class SMSOutOfBandProcessor(OutOfBandProcessor):
    """
    <oob>
        <sms>
            <recipient><get name="contacturi"/></recipient>
            <message><get name="messagebody"/></message>
        </sms>
    </oob>
    """
    def __init__(self):
        OutOfBandProcessor.__init__(self)
        self._recipient = None
        self._message = None

    def parse_oob_xml(self, oob: ET.Element):
        if oob is not None:
            for child in oob:
                if child.tag == 'recipient':
                    self._recipient = child.text
                elif child.tag == 'message':
                    self._message = child.text
                else:
                    YLogger.error(self, "Unknown child element [%s] in sms oob", child.tag)

            if self._recipient is not None and self._message is not None:
                return True

        YLogger.error(self, "Invalid sms oob command")
        return False

    def execute_oob_command(self, client_context):
        YLogger.info(client_context, "SMSOutOfBandProcessor: Messaging=%s", self._recipient)
        return "SMS"

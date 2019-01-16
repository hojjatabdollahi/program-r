from programr.utils.logging.ylogger import YLogger
import xml.etree.ElementTree as ET

from programr.oob.oob import OutOfBandProcessor


class EmailOutOfBandProcessor(OutOfBandProcessor):
    """
    <oob>
        <email>
            <to>recipient</to>
            <subject>subject text</subject>
            <body>body text</body>
        </email>
    </oob>
    """

    def __init__(self):
        OutOfBandProcessor.__init__(self)
        self._to = None
        self._subject = None
        self._body = None

    def parse_oob_xml(self, oob: ET.Element):
        if oob is not None:
            for child in oob:
                if child.tag == 'to':
                    self._to = child.text
                elif child.tag == 'subject':
                    self._subject = child.text
                elif child.tag == 'body':
                    self._body = child.text
                else:
                    YLogger.error(self, "Unknown child element [%s] in email oob", child.tag)

            if self._to is not None and \
                self._subject is not None and \
                self._body is not None:
                return True

        YLogger.error(self, "Invalid email oob command")
        return False

    def execute_oob_command(self, client_context):
        YLogger.info(client_context, "EmailOutOfBandProcessor: Emailing=%s", self._to)
        return "EMAIL"

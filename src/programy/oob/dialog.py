from programy.utils.logging.ylogger import YLogger
import xml.etree.ElementTree as ET

from programy.oob.oob import OutOfBandProcessor


class DialogOutOfBandProcessor(OutOfBandProcessor):
    """
    <oob>
        <dialog><title>Which contact?</title><list><get name="contactlist"/></list></dialog>
    </oob>
    """

    def __init__(self):
        OutOfBandProcessor.__init__(self)
        self._title = None
        self._list = None

    def parse_oob_xml(self, oob: ET.Element):
        if oob is not None:
            for child in oob:
                if child.tag == 'title':
                    self._title = child.text
                elif child.tag == 'list':
                    self._list = child.text
                else:
                    YLogger.error(self, "Unknown child element [%s] in dialog oob", child.tag)

            if self._title is not None and \
                self._list is not None:
                return True

        YLogger.error(self, "Invalid dialog oob command")
        return False

    def execute_oob_command(self, client_context):
        YLogger.info(client_context, "DialogOutOfBandProcessor: Dialog=%s", self._title)
        return "DIALOG"

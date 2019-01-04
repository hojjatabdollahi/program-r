from programr.utils.logging.ylogger import YLogger

from programr.oob.oob import OutOfBandProcessor


class CameraOutOfBandProcessor(OutOfBandProcessor):
    """
    <oob>
        <camera>on|off</camera>
    </oob>
    """

    def __init__(self):
        OutOfBandProcessor.__init__(self)
        self._command = None

    def parse_oob_xml(self, oob):
        if oob is not None and oob.text is not None:
            self._command = oob.text
            return True
        else:
            YLogger.error(self, "Invalid camera oob command - missing command")
            return False

    def execute_oob_command(self, client_context):
        YLogger.info(client_context, "CameraOutOfBandProcessor: Setting camera to=%s", self._command)
        return "CAMERA"

from programy.utils.logging.ylogger import YLogger

from programy.oob.oob import OutOfBandProcessor

class DefaultOutOfBandProcessor(OutOfBandProcessor):
    # Default OOB Processor consumes XML and returns nothing

    def __init__(self):
        OutOfBandProcessor.__init__(self)

    def execute_oob_command(self, client_context):
        YLogger.info(client_context, "Default OOB Processing....")
        if self._xml is not None:
            return ""
        return ""

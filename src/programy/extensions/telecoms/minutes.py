from programy.utils.logging.ylogger import YLogger

from programy.extensions.base import Extension


class TelecomMinutesExtension(Extension):

    # execute() is the interface that is called from the <extension> tag in the AIML
    def execute(self, context, data):
        YLogger.debug(context, "Telecom Minutes - Calling external service for with extra data [%s]", data)

        #
        # Add the logic to receive the phone minutes usage and format it into used and total
        #
        #

        return "0 0"

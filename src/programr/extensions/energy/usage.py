from programr.utils.logging.ylogger import YLogger

from programr.extensions.base import Extension


class EnergyUsageExtension(Extension):

    # execute() is the interface that is called from the <extension> tag in the AIML
    def execute(self, context, data):
        YLogger.debug(context, "Energy Usage - Calling external service for with extra data [%s]", data)

        #
        # Add the logic to receive the balance and format it into KWh for Gas and Electricity consumption
        #
        #

        return "0 0 KWh"

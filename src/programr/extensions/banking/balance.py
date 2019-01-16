from programr.utils.logging.ylogger import YLogger

from programr.extensions.base import Extension


class BankingBalanceExtension(Extension):

    # execute() is the interface that is called from the <extension> tag in the AIML
    def execute(self, context, data):
        YLogger.debug(context, "Bank Balance - Calling external service for with extra data [%s]", data)

        #
        # Add the logic to receive the balance and format it into pounds and pence and either CREDIT|DEBIT
        #
        #

        return "0 00 CREDIT"

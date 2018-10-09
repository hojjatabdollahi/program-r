from programy.utils.logging.ylogger import YLogger

from programy.processors.processing import PreProcessor

class ToUpperPreProcessor(PreProcessor):

    def __init__(self):
        PreProcessor.__init__(self)

    def process(self, context, word_string):
        YLogger.debug(context, "Making input upper case...")
        #return word_string.upper()
        return word_string

from programy.utils.logging.ylogger import YLogger
import emoji

from programy.processors.processing import PreProcessor

class DemojizePreProcessor(PreProcessor):

    def __init__(self):
        PreProcessor.__init__(self)

    def process(self, context, word_string):
        return emoji.demojize(word_string)

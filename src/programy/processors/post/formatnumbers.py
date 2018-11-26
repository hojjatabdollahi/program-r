from programy.utils.logging.ylogger import YLogger
import re

from programy.processors.processing import PostProcessor

class FormatNumbersPostProcessor(PostProcessor):
    def __init__(self):
        PostProcessor.__init__(self)

    def process(self, context, word_string):
        YLogger.debug(context, "Formatting numbers...")
        word_string = re.sub(r'(\d)([\.|,])\s+(\d)', r'\1\2\3', word_string)
        word_string = re.sub(r'(\d)\s+([\.|,])(\d)', r'\1\2\3', word_string)
        word_string = re.sub(r'(\d)\s+([\.|,])\s+(\d)', r'\1\2\3', word_string)
        return word_string

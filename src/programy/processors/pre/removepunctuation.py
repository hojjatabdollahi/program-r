from programy.utils.logging.ylogger import YLogger
from programy.processors.processing import PreProcessor
from programy.utils.text.text import TextUtils

class RemovePunctuationPreProcessor(PreProcessor):

    def __init__(self):
        PreProcessor.__init__(self)

    def process(self, context, word_string):
        YLogger.debug(context, "Removing punctuation...")
        return TextUtils.strip_all_punctuation(word_string)

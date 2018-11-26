from programy.utils.logging.ylogger import YLogger
import re

from programy.processors.processing import PreProcessor
from programy.utils.language.chinese import ChineseLanguage

class MergeChinesePostProcessor(PreProcessor):

    def __init__(self):
        PreProcessor.__init__(self)

    def process(self, context, word_string):
        YLogger.debug(context, "Merging Chinese into understandable words...")

        words = word_string.split(" ")
        str = ""
        for word in words:
            if ChineseLanguage.is_language(word):
                str += word
            else:
                str += " " + word + " "
        str = re.sub(r'\s+', ' ', str)
        return str.strip()


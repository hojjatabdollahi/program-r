from programy.utils.logging.ylogger import YLogger
import re

from programy.processors.processing import PreProcessor
from programy.utils.language.chinese import ChineseLanguage

class SplitChinesePreProcessor(PreProcessor):

    def __init__(self):
        PreProcessor.__init__(self)

    def process(self, context, word_string):
        YLogger.debug(context, "Splitting Chinese into parsable words...")
        chars = []
        for ch in word_string:
            if ChineseLanguage.is_language(ch):
                chars.append(" %s "%ch)
            else:
                chars.append(ch)
        text = "".join(chars).strip()
        return re.sub(' +',' ', text)

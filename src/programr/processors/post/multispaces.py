from programr.utils.logging.ylogger import YLogger
import re

from programr.processors.processing import PostProcessor

class RemoveMultiSpacePostProcessor(PostProcessor):
    def __init__(self):
        PostProcessor.__init__(self)

    def process(self, context, word_string):
        YLogger.debug(context, "Removing multiple spaces from words...")
        word_string = re.sub(r'\s+', ' ', word_string)
        return word_string.strip()

from programr.utils.logging.ylogger import YLogger
import re
import os

from programr.processors.processing import PostProcessor

class RemoveHTMLPostProcessor(PostProcessor):
    def __init__(self):
        PostProcessor.__init__(self)

    def process(self, context, word_string):
        YLogger.debug(context, "Removing html from sentence...")
        word_string = re.sub(r'\s*<\s*br\s*/>\s*', os.linesep, word_string)
        word_string = re.sub(r'\s*<br></br>\s*', os.linesep, word_string)
        return word_string

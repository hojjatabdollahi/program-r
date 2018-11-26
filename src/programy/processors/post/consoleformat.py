from programy.utils.logging.ylogger import YLogger
import textwrap
import os

from programy.processors.processing import PostProcessor

class ConsoleFormatPostProcessor(PostProcessor):
    def __init__(self):
        PostProcessor.__init__(self)

    def process(self, context, word_string):
        YLogger.debug(context, "Formatting response for console outpout...")
        lines = textwrap.wrap(word_string, width=80)
        word_string = os.linesep.join(lines)
        return word_string

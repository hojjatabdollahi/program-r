from programr.utils.logging.ylogger import YLogger

from programr.parser.template.nodes.base import TemplateNode
from programr.utils.text.text import TextUtils

class TemplateWordNode(TemplateNode):

    def __init__(self, word):
        TemplateNode.__init__(self)
        self._word = word

    @property
    def word(self):
        return self._word

    @word.setter
    def word(self, word):
        self._word = word

    def resolve(self, client_context):
        YLogger.debug(client_context, "[%s] resolved to [%s]", self.to_string(), self.word)
        if self.word is not None:
            return self.word
        return ""

    def to_string(self):
        return "[WORD]" + self.word

    def to_xml(self, client_context):
        return TextUtils.html_escape(self.word)

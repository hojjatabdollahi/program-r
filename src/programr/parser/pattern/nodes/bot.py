from programr.utils.logging.ylogger import YLogger
from programr.parser.pattern.nodes.base import PatternNode
from programr.parser.pattern.matcher import EqualsMatch
from programr.parser.exceptions import ParserException

class PatternBotNode(PatternNode):

    def __init__(self, attribs, text, userid='*'):
        PatternNode.__init__(self, userid)
        if 'name' in attribs:
            self._property = attribs['name']
        elif 'property' in attribs:
            self._property = attribs['property']
        elif text:
            self._property = text
        else:
            raise ParserException("Invalid bot node, neither name or property specified as attribute or text")

    def is_bot(self):
        return True

    @property
    def property(self):
        return self._property

    def to_xml(self, client_context, include_user=False):
        string = ""
        if include_user is True:
            string += '<bot userid="%s" property="%s">\n'%(self.userid, self.property)
        else:
            string += '<bot property="%s">\n' % self.property
        string += super(PatternBotNode, self).to_xml(client_context)
        string += "</bot>"
        return string

    def to_string(self, verbose=True):
        if verbose is True:
            return "BOT [%s] [%s] property=[%s]" % (self.userid, self._child_count(verbose), self.property)
        return "BOT property=[%s]" % (self.property)

    def equivalent(self, other):
        if other.is_bot():
            if self.userid == other.userid:
                if self.property == other.property:
                    return True
        return False

    def equals(self, client_context, words, word_no):
        word = words.word(word_no)

        if self.userid != '*':
            if self.userid != client_context.userid:
                return EqualsMatch(False, word_no)

        if client_context.brain.properties.has_property(self.property):
            if word == client_context.brain.properties.property(self.property):
                YLogger.debug(client_context, "Found word [%s] as bot property", word)
                return EqualsMatch(True, word_no, word)

        return EqualsMatch(False, word_no)

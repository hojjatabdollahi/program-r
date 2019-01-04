from programr.parser.exceptions import ParserException
from programr.parser.pattern.nodes.base import PatternNode
from programr.parser.pattern.matcher import EqualsMatch


class PatternWordNode(PatternNode):

    def __init__(self, word, userid='*'):
        PatternNode.__init__(self, userid)
        self._word = word

    def is_word(self):
        return True

    @property
    def word(self):
        return self._word

    def to_xml(self, client_context, include_user=False):
        string = ""
        if include_user:
            string += '<word userid="%s" word="%s">'%(self.userid, self.word)
        else:
            string += '<word word="%s">'% self.word
        string += super(PatternWordNode, self).to_xml(client_context, include_user)
        string += '</word>\n'
        return string

    def to_string(self, verbose=True):
        if verbose is True:
            return "WORD [%s] [%s] word=[%s]" % (self.userid, self._child_count(verbose), self.word)
        return "WORD [%s]" % (self.word)

    def can_add(self, new_node):
        if new_node.is_root():
            raise ParserException("Cannot add root node to child node")

    def equivalent(self, other):
        if other.is_word():
            if self.userid == other.userid:
                if self._word == other.word:
                    return True
        return False

    def equals(self, client_context, words, word_no):
        word = words.word(word_no)

        if self.userid != '*':
            if self.userid != client_context.userid:
                return EqualsMatch(False, word_no)

        return EqualsMatch(self.equals_ignore_case(self._word, word), word_no, word)

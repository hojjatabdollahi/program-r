from programr.parser.pattern.nodes.base import PatternNode
from programr.parser.pattern.matcher import EqualsMatch


class PatternPriorityWordNode(PatternNode):

    def __init__(self, word, userid='*'):
        PatternNode.__init__(self, userid)
        self._priority_word = word

    @property
    def priority_word(self):
        return self._priority_word

    def is_priority(self):
        return True

    def to_xml(self, client_context, include_user=False):
        string = ""
        if include_user is True:
            string += '<priority userid="%s" word="%s">'%(self.userid, self.priority_word)
        else:
            string += '<priority word="%s">'% self.priority_word
        string += super(PatternPriorityWordNode, self).to_xml(client_context)
        string += '</priority>\n'
        return string

    def to_string(self, verbose=True):
        if verbose is True:
            return "PWORD [%s] [%s] word=[%s]" % (self.userid, self._child_count(verbose), self.priority_word)
        return "PWORD [%s]" % (self.priority_word)

    def equivalent(self, other):
        if other.is_priority():
            if self.userid == other.userid:
                if self.priority_word == other.priority_word:
                    return True
        return False

    def equals(self, client_context, words, word_no):
        word = words.word(word_no)

        if self.userid != '*':
            if self.userid != client_context.userid:
                return EqualsMatch(False, word_no)

        if self.priority_word == word:
            return EqualsMatch(True, word_no, word)

        return EqualsMatch(False, word_no)


from programr.parser.exceptions import ParserException

from programr.parser.pattern.matcher import Match
from programr.parser.pattern.nodes.base import PatternNode


class PatternRootNode(PatternNode):

    def __init__(self, userid='*'):
        PatternNode.__init__(self, userid)

    def is_root(self):
        return True

    def can_add(self, new_node: PatternNode):
        if new_node.is_root():
            raise ParserException("Cannot add root node to existing root node")
        if new_node.is_topic():
            raise ParserException("Cannot add topic node to root node")
        if new_node.is_that():
            raise ParserException("Cannot add that node to root node")
        if new_node.is_template():
            raise ParserException("Cannot add template node to root node")

    def equivalent(self, other: PatternNode)->bool:
        if other.is_root():
            if self.userid == other.userid:
                return True
        return False

    def to_string(self, verbose: bool = True)->str:
        if verbose is True:
            return "ROOT [%s] [%s]" %(self.userid, self._child_count(verbose))
        return "ROOT "

    def match(self, client_context, context, words):
        return self.consume(client_context, context, words, 0, Match.WORD, 0)

    def _remove_priority(self, userid):
        removals = []
        for node in self._priority_words:
            if node.userid == userid:
                removals.append(node)
        for node in removals:
            self._remove_node(node)

    def _remove_0ormore_hash(self, userid):
        if self._0ormore_hash is not None:
            if self._0ormore_hash.userid == userid:
                self._remove_node(self._0ormore_hash)

    def _remove_1ormore_underline(self, userid):
        if self._1ormore_underline is not None:
            if self._1ormore_underline.userid == userid:
                self._remove_node(self._1ormore_underline)

    def _remove_children(self, userid):
        removals = []
        for node in self._children:
            if node.userid == userid:
                removals.append(node)
        for node in removals:
            self._remove_node(node)

    def _remove_0ormore_arrow(self, userid):
        if self._0ormore_arrow is not None:
            if self._0ormore_arrow.userid == userid:
                self._remove_node(self._0ormore_arrow)

    def _remove_1ormore_star(self, userid):
        if self._1ormore_star is not None:
            if self._1ormore_star.userid == userid:
                self._remove_node(self._1ormore_star)

    def remove_children_with_userid(self, userid):

        self._remove_priority(userid)

        self._remove_0ormore_hash(userid)

        self._remove_1ormore_underline(userid)

        self._remove_children(userid)

        self._remove_0ormore_arrow(userid)

        self._remove_1ormore_star(userid)



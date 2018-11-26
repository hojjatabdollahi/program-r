from programy.utils.logging.ylogger import YLogger

from programy.parser.exceptions import ParserException
from programy.parser.pattern.nodes.base import PatternNode
from programy.parser.pattern.nodes.topic import PatternTopicNode
from programy.parser.pattern.nodes.that import PatternThatNode


class PatternWildCardNode(PatternNode):

    def __init__(self, wildcard, userid='*'):
        PatternNode.__init__(self, userid)
        if wildcard not in self.matching_wildcards():
            raise ParserException("%s not in valid wildcards %s" % (wildcard, ", ".join(self.matching_wildcards())))
        self._wildcard = wildcard

    def is_wildcard(self):
        return True

    def can_add(self, new_node):
        if new_node.is_root():
            raise ParserException("Cannot add root node to child node")

    @property
    def wildcard(self):
        return self._wildcard

    def matching_wildcards(self):
        return []

    def invalid_topic_or_that(self, tabs, client_context, word, context, matches_add):
        if word == PatternTopicNode.TOPIC:
            YLogger.debug(client_context, "%sFound a topic at the wrong place....", tabs)
            context.pop_matches(matches_add)
            return True

        if word == PatternThatNode.THAT:
            YLogger.debug(client_context, "%sFound a that at the wrong place....", tabs)
            context.pop_matches(matches_add)
            return True

        return False

    def check_child_is_wildcard(self, tabs, client_context, context, words, word_no, match_type, depth):
        if self._0ormore_hash is not None:
            YLogger.debug(client_context, "%sWildcard # is next node, moving on!", tabs)
            match = self._0ormore_hash.consume(client_context, context, words, word_no+1, match_type, depth+1)
            if match is not None:
                return match

        if self._1ormore_underline is not None:
            YLogger.debug(client_context, "%sWildcard _ is next node, moving on!", tabs)
            match = self._1ormore_underline.consume(client_context, context, words, word_no+1, match_type, depth+1)
            if match is not None:
                return match

        if self._0ormore_arrow is not None:
            YLogger.debug(client_context, "%sWildcard ^ is next node, moving on!", tabs)
            match = self._0ormore_arrow.consume(client_context, context, words, word_no+1, match_type, depth+1)
            if match is not None:
                return match

        if self._1ormore_star is not None:
            YLogger.debug(client_context, "%sWildcard * is next node, moving on!", tabs)
            match = self._1ormore_star.consume(client_context, context, words, word_no+1, match_type, depth+1)
            if match is not None:
                return match

        return None

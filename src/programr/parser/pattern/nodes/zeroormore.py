from programr.utils.logging.ylogger import YLogger

from programr.parser.pattern.nodes.wildcard import PatternWildCardNode
from programr.parser.pattern.matcher import Match

class PatternZeroOrMoreWildCardNode(PatternWildCardNode):

    MATCH_CHARS = ['^', '#']

    def __init__(self, wildcard, userid='*'):
        PatternWildCardNode.__init__(self, wildcard, userid)

    def is_zero_or_more(self):
        return True

    def matching_wildcards(self):
        return PatternZeroOrMoreWildCardNode.MATCH_CHARS

    @staticmethod
    def is_wild_card(text):
        return bool(text in PatternZeroOrMoreWildCardNode.MATCH_CHARS)

    def to_xml(self, client_context, include_user=False):
        string = ""
        if include_user is True:
            string += '<zerormore userid="%s" wildcard="%s">\n'%(self.userid, self.wildcard)
        else:
            string += '<zerormore wildcard="%s">\n' % self.wildcard
        string += super(PatternZeroOrMoreWildCardNode, self).to_xml(client_context)
        string += "</zerormore>\n"
        return string

    def to_string(self, verbose=True):
        if verbose is True:
            return "ZEROORMORE [%s] [%s] wildcard=[%s]" % (self.userid, self._child_count(verbose), self.wildcard)
        return "ZEROORMORE [%s]" % (self.wildcard)

    def equivalent(self, other):
        if other.is_zero_or_more():
            if self.userid == other.userid:
                if self._wildcard == other.wildcard:
                    return True
        return False

    def consume(self, client_context, context, words, word_no, match_type, depth):

        tabs = self.get_tabs(client_context, depth)

        #TODO uncomment this section
        # if context.search_time_exceeded() is True:
        #     YLogger.error(client_context, "%sMax search time [%d]secs exceeded", tabs, context.max_search_timeout)
        #     return None

        if context.search_depth_exceeded(depth) is True:
            YLogger.error(client_context, "%sMax search depth [%d] exceeded", tabs, context.max_search_depth)
            return None

        context_match = Match(match_type, self, None)
        context.add_match(context_match)
        matches_added = 1

        match = self.check_child_is_wildcard(tabs, client_context, context, words, word_no, match_type, depth)
        if match is not None:
            return match

        word = words.word(word_no)

        if self._children:
            for child in self._children:

                result = child.equals(client_context, words, word_no)
                if result.matched is True:
                    word_no = result.word_no
                    YLogger.debug(client_context, "%sWildcard child matched %s", tabs, result.matched_phrase)

                    context_match2 = Match(Match.WORD, child, result.matched_phrase)

                    context.add_match(context_match2)
                    matches_added += 1

                    match = child.consume(client_context, context, words, word_no+1, match_type, depth+1)
                    if match is not None:
                        return match

                    if self.invalid_topic_or_that(tabs, client_context, word, context, matches_added) is True:
                        return None

            YLogger.debug(client_context, "%sWildcard %s matched %s", tabs, self._wildcard, word)
            context_match.add_word(word)

            match = super(PatternZeroOrMoreWildCardNode, self).consume(client_context, context, words, word_no + 1, match_type, depth+1)
            if match is not None:
                return match

            word_no += 1
            word = words.word(word_no)

            if self.invalid_topic_or_that(tabs, client_context, word, context, matches_added) is True:
                return None

            YLogger.debug(client_context, "%sWildcard %s matched %s", tabs, self._wildcard, word)
            context_match.add_word(word)

            match = super(PatternZeroOrMoreWildCardNode, self).consume(client_context, context, words, word_no + 1, match_type, depth+1)
            if match is not None:
                return match

            word_no += 1
            if word_no >= words.num_words():
                context.pop_matches(matches_added)
                return None
            word = words.word(word_no)

        YLogger.debug(client_context, "%sNo children, consume words until next break point", tabs)
        while word_no < words.num_words() - 1:
            match = super(PatternZeroOrMoreWildCardNode, self).consume(client_context, context, words, word_no, match_type, depth+1)
            if match is not None:
                return match

            if self.invalid_topic_or_that(tabs, client_context, word, context, matches_added) is True:
                return None

            YLogger.debug(client_context, "%sWildcard %s matched %s", tabs, self._wildcard, word)
            context_match.add_word(word)

            word_no += 1
            word = words.word(word_no)

        match = super(PatternZeroOrMoreWildCardNode, self).consume(client_context, context, words, word_no, match_type,
                                                                   depth + 1)

        if match is not None:
            return match
        context.pop_matches(matches_added)
        return None

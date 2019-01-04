import unittest

from programr.bot import Bot
from programr.dialog.dialog import Question, Sentence
from programr.parser.pattern.matcher import MatchContext, Match
from programr.parser.pattern.nodes.oneormore import PatternOneOrMoreWildCardNode
from programr.config.bot.bot import BotConfiguration
from programr.context import ClientContext

from programrtest.aiml_tests.client import TestClient

class TemplateGraphTestClient(unittest.TestCase):

    def setUp(self):

        self._client_context = ClientContext(TestClient(), "testid")
        self._client_context.bot = Bot(BotConfiguration())
        self._client_context.brain = self._client_context.bot.brain

        self._graph = self._client_context.bot.brain.aiml_parser.template_parser

        self.test_sentence = Sentence(self._client_context.brain.nlp.tokenizer, "test sentence")

        test_node = PatternOneOrMoreWildCardNode("*")

        self.test_sentence._matched_context = MatchContext(max_search_depth=100, max_search_timeout=-1, tokenizer=self._client_context.brain.nlp.tokenizer)
        self.test_sentence._matched_context._matched_nodes = [Match(Match.WORD, test_node, 'one'),
                                                              Match(Match.WORD, test_node, 'two'),
                                                              Match(Match.WORD, test_node, 'three'),
                                                              Match(Match.WORD, test_node, 'four'),
                                                              Match(Match.WORD, test_node, 'five'),
                                                              Match(Match.WORD, test_node, 'six'),
                                                              Match(Match.TOPIC, test_node, '*'),
                                                              Match(Match.THAT, test_node, '*')]

        conversation = self._client_context.bot.get_conversation(self._client_context)
        question = Question.create_from_sentence(self.test_sentence)
        conversation._questions.append(question)

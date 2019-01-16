import unittest
from programr.processors.pre.removepunctuation import RemovePunctuationPreProcessor
from programr.processors.pre.toupper import ToUpperPreProcessor
from programr.processors.pre.normalize import NormalizePreProcessor
from programr.processors.pre.demojize import DemojizePreProcessor
from programr.bot import Bot
from programr.config.bot.bot import BotConfiguration
from programr.context import ClientContext

from programrtest.aiml_tests.client import TestClient


class PreProcessingTests(unittest.TestCase):

    def test_pre_cleanup(self):

        context = ClientContext(TestClient(), "testid")
        context.bot = Bot(config=BotConfiguration())
        context.brain = context.bot.brain
        test_str = "This is my Location!"

        punctuation_processor = RemovePunctuationPreProcessor()
        test_str = punctuation_processor.process(context, test_str)
        self.assertEqual("This is my Location", test_str)

        normalize_processor = NormalizePreProcessor()
        test_str = normalize_processor.process(context, test_str)
        self.assertEqual("This is my Location", test_str)

        toupper_processor = ToUpperPreProcessor()
        test_str = toupper_processor.process(context, test_str)
        self.assertEqual("THIS IS MY LOCATION", test_str)

        demojize_processpr = DemojizePreProcessor()
        test_str = demojize_processpr.process(context, test_str)
        self.assertEqual(test_str, test_str)
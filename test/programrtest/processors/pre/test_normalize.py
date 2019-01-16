import unittest
from programr.processors.pre.normalize import NormalizePreProcessor
from programr.bot import Bot
from programr.config.bot.bot import BotConfiguration
from programr.context import ClientContext

from programrtest.aiml_tests.client import TestClient


class NormalizeTests(unittest.TestCase):

    def setUp(self):
        self.bot = Bot(config=BotConfiguration())

    def test_normalize(self):
        processor = NormalizePreProcessor()

        context = ClientContext(TestClient(), "testid")
        context.bot = self.bot
        context.brain = self.bot.brain

        result = processor.process(context, "Hello")
        self.assertIsNotNone(result)
        self.assertEqual("Hello", result)

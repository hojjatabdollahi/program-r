import unittest
from programr.processors.post.denormalize import DenormalizePostProcessor
from programr.bot import Bot
from programr.brain import Brain
from programr.config.brain.brain import BrainConfiguration
from programr.config.bot.bot import BotConfiguration
from programr.context import ClientContext

from programrtest.aiml_tests.client import TestClient


class DenormalizeTests(unittest.TestCase):

    def setUp(self):
        self.bot = Bot(config=BotConfiguration())
        self.bot.brain.denormals.process_splits([" dot com ",".com"])

    def test_denormalize(self):
        processor = DenormalizePostProcessor ()

        context = ClientContext(TestClient(), "testid")
        context.bot = self.bot
        context.brain = self.bot.brain
        result = processor.process(context, "Hello")
        self.assertIsNotNone(result)
        self.assertEqual("Hello", result)

        result = processor.process(context, "hello dot com")
        self.assertIsNotNone(result)
        self.assertEqual("hello.com", result)
